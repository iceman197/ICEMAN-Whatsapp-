const express = require("express");
const cors = require("cors");
const OpenAI = require("openai");

const app = express();

app.use(cors());
app.use(express.json());

const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

app.post("/chat", async (req, res) => {
    try {
        const userMessage = req.body.message;

        const response = await client.responses.create({
            model: "gpt-5-mini",
            input: [
                {
                    role: "system",
                    content: "You are Nana Yaw AI, the friendly AI assistant on Nana Yaw's official website."
                },
                {
                    role: "user",
                    content: userMessage
                }
            ]
        });

        res.json({
            reply: response.output_text
        });

    } catch (error) {
        console.error(error);
        res.status(500).json({
            reply: "Sorry, Nana Yaw AI is temporarily unavailable."
        });
    }
});

app.listen(3000, () => {
    console.log("Nana Yaw AI server is running on port 3000");
});