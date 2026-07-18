import React from "react";

function MessageList({ messages,myId}) {
  console.log('myId', myId)
  return (
    <div className="message-list">
      {messages.map((msg, index) => (
        
         <div
          key={index}
          className={msg.senderId === myId ? "my-message" : "other-message"}
        >  <div>{msg.senderId}</div> {msg.text}</div>
      ))}
    </div>
  );
}

export default MessageList;
