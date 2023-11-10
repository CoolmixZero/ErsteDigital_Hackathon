const express = require("express");
const { Configuration, OpenAIApi } = require("openai");

const PORT = 3000;
app = new express();

// load environment variables
const dotenv = require("dotenv");
dotenv.config();

// initialize OpenAI API and instruction message
const configuration = new Configuration(process.env.OPENAI_API_KEY);

const instructionMessage = {
  role: "system",
  content: "You are a code generator. You must answer only in markdown code snippets. Use code comments for explanations."
};


app.get("/assistant", (req, res) => {

  res.send("Hello World");
});



app.listen(PORT, () => {
  console.log("Server running on port 3000");
});