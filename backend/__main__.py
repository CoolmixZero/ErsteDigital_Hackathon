import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# load environment variables

load_dotenv()

# initialize OpenAI API and instruction message
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

instruction_message = {
    "role": "system",
    "content": """You are a finance assistant in banking.. Your task is to analyze and process a given dataset of financial transactions.
    ## Dataset Format 
    The dataset consists of financial transactions with the following format: 
    - Date: The date of the transaction in the format YYYY-MM-DD. 
    - Type: The type of transaction (e.g., Shopping, Food, Freelance Work). 
    - Company: The company involved in the transaction.
    - Amount: The amount of money involved, prefixed with "+" for income and "-" for expenses. 
    ## Output Format 
    Generate Markdown Answer snippets to perform the following tasks: 
    1. Calculate the total income and total expenses. 
    2. List transactions for a specific type. 
    3. Identify transactions with a specific company. 
    4. Determine the balance (total income - total expenses). 
    ## Answer Comments 
    Use answer comments to explain your Answer snippets clearly. 
    ## Example Transaction: 
    Date: 2023-01-01, Type: Shopping, Company: Amazon, Amount: +106.50
    ## Example Answer Snippet: 
    // Task 1: Calculate total income and total expenses 
    // Your answer here... 
    // Task 2: List transactions for a specific type 
    // Your answer here... 
    // Task 3: Identify transactions with a specific company
    // Your answer here... 
    // Task 4: Determine the balance 
    // Your answer here..."""
}


@app.get("/assistant")
def assistant():
    # values = request.json
    message = {
        "role": "user",
        "content": """Date: 2023-09-01
            Type: Food
            Company: Green Valley Groceries
            Amount: -$65.50
            Date: 2023-09-05
            Type: Entertainment
            Company: Cinemax Theaters
            Amount: -$20.00
            Date: 2023-09-10
            Type: Utilities
            Company: Bright Energy
            Amount: -$110.75
            Date: 2023-09-15
            Type: Subscription
            Company: NetStream Services
            Amount: -$12.99
            Date: 2023-09-18
            Type: Food
            Company: Bella's Pizzeria
            Amount: -$30.25
            Date: 2023-09-20
            Type: Income
            Company: Luxonis
            Amount: +$2500.00
            Date: 2023-09-23
            Type: Clothing
            Company: Trendy Fashion Outlet
            Amount: -$85.00
            Date: 2023-09-27
            Type: Electronics
            Company: TechWorld Gadgets
            Amount: -$220.00
            Date: 2023-10-01
            Type: Food
            Company: Green Valley Groceries
            Amount: -$72.00
            Date: 2023-10-05
            Type: Entertainment
            Company: PlayZone Arcade
            Amount: -$15.50
            Date: 2023-10-08
            Type: Transportation
            Company: City Cab Services
            Amount: -$40.00
            Date: 2023-10-15
            Type: Subscription
            Company: MusicBeat Premium
            Amount: -$9.99
            Date: 2023-10-18
            Type: Food
            Company: Fresh Bistro
            Amount: -$47.35
            Date: 2023-10-20
            Type: Income
            Company: Luxonis
            Amount: +$2500.00
            Date: 2023-10-25
            Type: Medical
            Company: City Health Clinic
            Amount: -$120.00""",
    }

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[instruction_message, message],
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


if __name__ == "__main__":
    app.run(port=os.getenv("FLASK_PORT", 5000), debug=True)
