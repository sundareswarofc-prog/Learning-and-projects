const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const { OAuth2Client } = require("google-auth-library");
require('dotenv').config();


const app = express();
app.use(cors());
app.use(bodyParser.json());

const client = new OAuth2Client(process.env.CLIENT_ID);

app.post("/auth/google", async (req, res) => {
  const { token } = req.body;

  try {
    const ticket = await client.verifyIdToken({
      idToken: token,
      audience: process.env.CLIENT_ID,
    });
    const payload = ticket.getPayload();

    console.log("User Info:", payload);
    res.json({ success: true, user: payload });
  } catch (err) {
    res.status(400).json({ success: false, error: "Invalid token" });
  }
});

app.listen(5000, () => console.log("Server running on http://localhost:5000"));
