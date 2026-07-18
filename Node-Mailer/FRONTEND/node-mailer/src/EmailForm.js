import React, { useState } from "react";
import axios from "axios";

export default function EmailForm() {
  const [to, setTo] = useState("");
  const [subject, setSubject] = useState("");
  const [text, setText] = useState("");
  const [status, setStatus] = useState("");

  const sendEmail = async () => {
    try {
      const response = await axios.post("http://localhost:5000/send-email", {
        to,
        subject,
        text
      });
      if (response.data.success) {
        setStatus("Email sent successfully!");
      } else {
        setStatus("Failed to send email.");
      }
    } catch (err) {
      console.error(err);
      setStatus("Error sending email");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Send Email</h2>
      <input
        type="email"
        placeholder="Recipient"
        value={to}
        onChange={(e) => setTo(e.target.value)}
      /><br/>
      <input
        type="text"
        placeholder="Subject"
        value={subject}
        onChange={(e) => setSubject(e.target.value)}
      /><br/>
      <textarea
        placeholder="Message"
        value={text}
        onChange={(e) => setText(e.target.value)}
      /><br/>
      <button onClick={sendEmail}>Send</button>
      <p>{status}</p>
    </div>
  );
}
