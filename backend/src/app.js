const express = require("express");
import cors from 'cors';

const { OpenAI } = require('openai');

app = new express();
app.use(cors());

// load environment variables
const dotenv = require("dotenv");
dotenv.config();

// initialize OpenAI API and instruction message
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY // This is also the default, can be omitted
});

const instructionMessage = {
  role: "system",
  content: "OpenAI Code Generation Instructions \
  \
  ## Task Description \
  You are a code generator. Your task is to analyze and process a given dataset of financial transactions. \
  \
  ## Dataset Format \
  The dataset consists of financial transactions with the following format: \
  - Date: The date of the transaction in the format YYYY-MM-DD. \
  - Type: The type of transaction (e.g., Shopping, Food, Freelance Work). \
  - Company: The company involved in the transaction.\
  - Amount: The amount of money involved, prefixed with "+" for income and "-" for expenses. \
  \
  ## Output Format \
  Generate Markdown code snippets to perform the following tasks: \
  1. Calculate the total income and total expenses. \
  2. List transactions for a specific type. \
  3. Identify transactions with a specific company. \
  4. Determine the balance (total income - total expenses). \
  \
  ## Code Comments \
  Use code comments to explain your code snippets clearly. \
  \
  ## Example Transaction: \
  Date: 2023-01-01, Type: Shopping, Company: Amazon, Amount: +106.50 \
  \
  ## Example Code Snippet: \
  // Task 1: Calculate total income and total expenses \
  // Your code here... \
  \
  // Task 2: List transactions for a specific type \
  // Your code here... \
  \
  // Task 3: Identify transactions with a specific company \
  // Your code here... \
  \
  // Task 4: Determine the balance \
  // Your code here..."
};


app.get("/assistant", async (req, res) => {
  // const body = await req.body;
  // const { message } = body;

  const chatCompletion = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [instructionMessage],
    // messages: [instructionMessage, ...message],
  });

  console.log(chatCompletion);
  res.send(chatCompletion.choices[0].message);
  // return chatCompletion.choices[0].message;
});

app.listen(process.env.EXPRESS_PORT, () => {
  console.log("Server running on port 3000");
});