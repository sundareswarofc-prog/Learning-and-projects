import React, { useState } from 'react';
import { Form, Input, Button, Checkbox, Card, Typography, Spin } from 'antd';
import './Auth.css';
import { Link, useNavigate } from 'react-router-dom';

const { Title, Text } = Typography;

const Login = () => {

  const navigate = useNavigate()
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [errorMessage, setErrorMessage] = useState({
    emailError: false,
    passwordError: false
  })
  const [spinner, setSpinner] = useState(false)

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
    setErrorMessage({
      emailError: false,
      passwordError: false
    })
    switch (field) {
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

  const getInput = deBounce(setInputvalues, 300)

  const handleSubmit = async (e) => {
    if (!email.length ){
      setErrorMessage((prev) => ({ ...prev, emailError: "Enter the email" }))
    }
    if (!password.length ){
      setErrorMessage((prev) => ({ ...prev, passwordError: "Enter the password" }))
    }

    const useLoginData = {
      email,
      password
    }

    if (email && password) {
      try {
        setSpinner(true)
        const response = await fetch("http://localhost:5000/login", {
          method: "post",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(useLoginData)
        })
        const data = await response.json();
        if (!data.message) {
          setSpinner(false)
          alert(data?.message || "Login failed");
          return;
        }

        if (data?.message == "User not found") {
          setSpinner(false)
          setErrorMessage((prev) => ({ ...prev, emailError: "User not found" }))
        }

        if (data?.message == "Invalid password") {
          setSpinner(false)
          setErrorMessage((prev) => ({ ...prev, passwordError: "Invalid password" }))
        }

        if (data?.message == "OTP sent successfully") {
          setSpinner(false)
          navigate("/otp", {
            state: {
              email
            }
          })
        }

      }
      catch (err) {
        setSpinner(false)
        console.error(err);
      }
    }
  }

  return (
    <Spin spinning={spinner} size={"large"}>
      <div className="auth-page">
        <Card className="auth-card">
          <Title level={3} className="auth-title">Sign In</Title>
          <Form name="login" layout="vertical">
            <Form.Item
              name="email"
              label="Email"
              // rules={[{ required: true, message: 'Please input your email!' }, { type: 'email', message: 'Enter a valid email' }]}
            >
              <Input placeholder="you@example.com" onChange={(e) => getInput(e.target.value, "email")} status={errorMessage.emailError ? "error" : " "} />
              <div style={{ color: "red", display: errorMessage.emailError ? "block" : "none" }} >{errorMessage.emailError}</div>
            </Form.Item>

            <Form.Item
              name="password"
              label="Password"
               validateTrigger="onChange"
              // rules={[{ required: true, message: 'Please input your password!' }]}
            >
              <Input.Password placeholder="••••••••" onChange={(e) => getInput(e.target.value, "password")} status={errorMessage.passwordError ? "error" : " "} />
              <div style={{ color: "red", display: errorMessage.passwordError ? "block" : "none" }} >Wrong password</div>
            </Form.Item>


            <Form.Item name="remember" valuePropName="checked">
              <Checkbox>Remember me</Checkbox>
            </Form.Item>

            <Form.Item>
              <Button type="primary" htmlType="submit" block onClick={(e) => handleSubmit(e)}>
                Sign In
              </Button>
            </Form.Item>

            <div className="auth-footer">
              <Text>
                Don't have an account? <Link to="signup">Sign up</Link>
              </Text>
              <a className="auth-forgot" href="#forgot">Forgot password?</a>
            </div>
          </Form>
        </Card>
      </div>
    </Spin>
  );
};

export default Login;
