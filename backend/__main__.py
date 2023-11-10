import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

from utils import sequence_prediction

app = Flask(__name__)
CORS(app)

# load environment variables

load_dotenv()

# initialize OpenAI API and instruction message
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ! TODO: add to dataset date and priority columns! 
instruction_message = {
    "role": "system",
    "content": """
    You are a Finance Assistant who is giving advice through client transaction history. 
    Your role is to help to navigate and manage client finances with ease. 
    Dataset Format is next:
    1. Type - the category of the transaction (e.g., Shopping, Food, Freelance Work);
    2. Amount - the monetary value, with "+" indicating income and "-" indicating expenses.
    Use client transaction history in your response to indicate to a field, where he can save money (and also tell him an amount that he can save).
    All transaction are going to be in the next message.
    """
}


@app.get("/assistant")
def assistant():
    # values = request.json
    messages = [
        {
            "role": "user",
            "content": """
            Client transaction history (json format):
            [
                {
                    Type: Food,
                    Amount: -$65.50
                },
                {
                    Type: Entertainment,
                    Amount: -$20.00
                },
                {
                    Type: Utilities,
                    Amount: -$110.75
                },
                {
                    Type: Subscription,
                    Amount: -$12.99
                },
                {
                    Type: Food,
                    Amount: -$30.25
                },
                {
                    Type: Income,
                    Amount: +$2500.00
                },
                {
                    Type: Clothing,
                    Amount: -$85.00
                },
                {
                    Type: Electronics,
                    Amount: -$220.00
                },
                {
                    Type: Food,
                    Amount: -$72.00
                },
                {
                    Type: Entertainment,
                    Amount: -$15.50
                },
                {
                    Type: Transportation,
                    Amount: -$40.00
                },
                {
                    Type: Subscription,
                    Amount: -$9.99
                },
                {
                    Type: Food,
                    Amount: -$47.35
                },
                {
                    Type: Income,
                    Amount: +$2500.00
                },
                {
                    Type: Medical,
                    Amount: -$120.00
                }
            ]
            # Client question: How can I safe more money?"""
        }
    ]

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[instruction_message, *messages],
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

@app.get("/forecast")
def forecast():
    return jsonify(sequence_prediction())

if __name__ == "__main__":
    app.run(port=os.getenv("FLASK_PORT", 5000), debug=True)
