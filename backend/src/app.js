const express = require("express");
const { OpenAI } = require('openai');

const PORT = 3000;
app = new express();

// load environment variables
const dotenv = require("dotenv");
dotenv.config();

// initialize OpenAI API and instruction message
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY // This is also the default, can be omitted
});

const instructionMessage = {
  role: "system",
  content: "You are a code generator. You must answer only in markdown code snippets. Use code comments for explanations."
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

app.listen(PORT, () => {
  console.log("Server running on port 3000");
});