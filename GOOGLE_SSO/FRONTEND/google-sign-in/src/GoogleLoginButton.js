import React from "react";
import { GoogleOAuthProvider, GoogleLogin } from "@react-oauth/google";
import axios from "axios";

const GoogleLoginButton = () => {
  const handleSuccess = async (credentialResponse) => {
    console.log("Google Token:", credentialResponse);

    // Send token to backend
    try {
      const res = await axios.post("http://localhost:5000/auth/google", {
        token: credentialResponse.credential,
      });
      console.log("Backend Response:", res.data);
    } catch (error) {
      console.error("Error sending token:", error);
    }
  };

  return (
    <GoogleOAuthProvider clientId="528481642260-8q2j49isg3brp2t35ll3qcrsfu4ok1ao.apps.googleusercontent.com">
      <GoogleLogin
        onSuccess={handleSuccess}
        onError={() => {
          console.log("Login Failed");
        }}
      />
    </GoogleOAuthProvider>
  );
};

export default GoogleLoginButton;
