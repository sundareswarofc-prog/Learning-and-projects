import React, { useState, useEffect, useRef } from "react";
import MessageList from "./MessageList";
import MessageInput from "./MessageInput";

function Chat() {
  const [messages, setMessages] = useState([]);
  const ws = useRef(null);
  const [myId, setMyId] = useState(null);

  useEffect(() => {
    ws.current = new WebSocket("ws://localhost:8080");

    ws.current.onmessage = (event) => {
  if (event.data instanceof Blob) {
    event.data.text().then(text => {
      const data = JSON.parse(text); // parse only after converting blob to text
      handleMessage(data);
    });
  } else {
    const data = JSON.parse(event.data); // directly parse if already a string
    handleMessage(data);
  }
};

function handleMessage(data) {
  if (!myId && data.senderId) {
    setMyId(data.senderId);
  }
  setMessages(prev => [...prev, data]);
}

    
    return () => ws.current.close();
  }, []);

  const sendMessage = (msg) => {
    if (ws.current && msg.trim() !== "") {
      ws.current.send(msg);
    }
  };
  console.log('messages', messages)

  return (
    <div className="chat-container">
      <MessageList messages={messages} myId={myId} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
}

export default Chat;
