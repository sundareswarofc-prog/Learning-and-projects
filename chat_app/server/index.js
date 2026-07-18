// server/index.js
const WebSocket = require("ws");
const http = require("http");

const server = http.createServer();
const wss = new WebSocket.Server({ server });

function generateId() {
  return Math.random().toString(36).substring(2, 8); 
}

wss.on("connection", (ws) => {
  console.log("New client connected");
  ws.id = generateId();

  ws.on("message", (message) => {
    console.log("Received:", message.toString());

    const payload = JSON.stringify({
      senderId: ws.id,
      text: message.toString()
    });

    wss.clients.forEach((client) => {
      console.log('payload', payload)
      if (client.readyState === WebSocket.OPEN) {
        client.send(payload);
      }
    });
  });

  ws.on("close", () => {
    console.log("Client disconnected");
  });
});

server.listen(8080, () => {
  console.log("WebSocket server running at ws://localhost:8080");
});
