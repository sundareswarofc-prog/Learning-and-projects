import React from 'react';
import { Form, Input, Button, Card, Typography } from 'antd';
import './Auth.css';
import { Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';

const { Title, Text } = Typography;

const Signup = () => {

  const [fullName, setFullName] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [error,setError]=useState({
    email:false,
    password:false,
    name:false,
  })
  const navigate=useNavigate()
  const deBounce = (handleChange, delay) => {
    let timer;
    return (input, field) => {
      clearTimeout(timer)
      timer = setTimeout(() => {
        handleChange(input, field)
      }, delay)
    }
  }

  const setInputvalues = (input, field) => {
    setError({
    email:false,
    password:false,
    name:false,
  })
    switch (field) {
      case "name":
        setFullName(input);
        break;
      case "email":
        setEmail(input);
        break;
      case "password":
        setPassword(input);
        break;
      default:
        console.log("unknown field")
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if(!fullName){
      setError((prev)=>({...prev,name:"Enter the Name!"}))
    }
    if(!email){
      setError((prev)=>({...prev,email:"Enter the Email!"}))
    }
    if(!password){
      setError((prev)=>({...prev,password:"Enter the password!"}))
    }

    const useSignUpData = {
      fullName,
      email,
      password
    }

    try {
      const response = await fetch("http://localhost:5000/signup", {
        method: "post",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(useSignUpData)
      })
      const data = await response.json();
      console.log(data)
        if(data.success){
          console.log("test signup")
          localStorage.setItem("token", data.token);
          navigate("/homepage")
        }
    }
    catch (err) {
      console.error(err);
    }

  }

  const getInputValues = deBounce(setInputvalues, 300)

  return (
    <div className="auth-page">
      <Card className="auth-card">
        <Title level={3} className="auth-title">Create Account</Title>
        <Form name="signup" layout="vertical">
          <Form.Item
            name="name"
            label="Full Name"
            rules={[{ required: true, message: 'Please input your name!' }]}
          >
            <Input placeholder="Your full name" onChange={(e) => getInputValues(e.target.value, "name")} />
            <div style={{ color: "red", display: error.name ? "block" : "none" }} >{error.name}</div>

          </Form.Item>

          <Form.Item
            name="email"
            label="Email"
            rules={[{ required: true, message: 'Please input your email!' }, { type: 'email', message: 'Enter a valid email' }]}
          >
            <Input placeholder="you@example.com" onChange={(e) => getInputValues(e.target.value, "email")} />
            <div style={{ color: "red", display: error.email ? "block" : "none" }} >{error.email}</div>
          </Form.Item>

          <Form.Item
            name="password"
            label="Password"
            rules={[{ required: true, message: 'Please create a password!' }]}
          >
            <Input.Password placeholder="Create a password" />
            <div style={{ color: "red", display: error.password ? "block" : "none" }} >{error.password}</div>

          </Form.Item>

          <Form.Item
            name="confirm"
            label="Confirm Password"
            dependencies={["password"]}
            rules={[{ required: true, message: 'Please confirm your password!' }]}
          >
            <Input.Password placeholder="Confirm password" onChange={(e) => getInputValues(e.target.value, "password")} />
            <div style={{ color: "red", display: error.password ? "block" : "none" }} >{error.password}</div>
          </Form.Item>

          <Form.Item>
            <Button type="primary" htmlType="submit" block onClick={handleSubmit}>
              Sign Up
            </Button>
          </Form.Item>

          <div className="auth-footer">
            <Text>
              Already have an account? <Link to="/">Sign in</Link>
            </Text>
          </div>
        </Form>
      </Card>
    </div>
  );
};

export default Signup;
