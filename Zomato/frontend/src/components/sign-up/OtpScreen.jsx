import { Button, Card, Flex, Input, message, Typography } from 'antd';
import { useState } from 'react';
import { useLocation, useNavigate } from "react-router-dom";



const { Title, Text } = Typography;

export const OtpScreen = () => {

    const location = useLocation();
    const email = location.state?.email;
    const [otp, setOtp] = useState("")
    const [spinner,setSpinner]=useState(false)
    const [error,setError]=useState(false)
    const navigate = useNavigate();

    const handleCheckOtp = async (e) => {
        if(!otp){
            setError(true)
        }
        e.preventDefault();
        try {
            const response = await fetch("http://localhost:5000/verify-otp", {
                method: "post",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email,
                    otp
                })
            })
            const data = await response.json();
            if (data.message == "Login successful") {
                localStorage.setItem("token", data.token);
                navigate("/homepage");
            }
        }
        catch (err) {
            console.log(err)
        }
    }

    const handleResendOTP = async (e) => {
        e.preventDefault();
        setSpinner(true)
        try {
            const response=await fetch("http://localhost:5000/login",{
                method: "post",
                headers: {
                "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email,
                    otp
                })
            })
            const data=await response.json();
            if(data.message=="OTP sent successfully"){
             setSpinner(false)
             message.success("OTP sent successfully");
            }
        }
        catch(err) {
         console.log(err);
        }
    }
    console.log(error,otp)

    return (
        <Flex
            justify="center"
            align="center"
            style={{ minHeight: '100vh', background: '#f5f5f5', padding: '24px' }}
        >
            <Card style={{ width: '100%', maxWidth: 420, borderRadius: 16, boxShadow: '0 8px 24px rgba(0,0,0,0.08)' }}>
                <Flex vertical align="center" gap="middle">
                    <Title level={2} style={{ marginBottom: 0 }}>Verify OTP</Title>
                    <Text type="secondary">Enter the 6-digit code sent to your phone</Text>

                    <Input.OTP length={6} style={{ marginTop: 8 }} onChange={(value) => {setOtp(value);setError(false)}} status={error?"error": " "}/>
                    <div style={{color:"red",display:error?"block":"none"}} >Wrong password</div>


                    <Button type="primary" style={{ width: '100%', height: 44, borderRadius: 10 }} onClick={handleCheckOtp}>
                        Verify
                    </Button>

                    <Text type="secondary">
                        Didn't receive OTP? <Text strong style={{ color: '#ff4d4f', cursor: 'pointer' }} onClick={handleResendOTP}>Resend</Text>
                    </Text>
                </Flex>
            </Card>
        </Flex>
    );
};