import { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ children }) => {
    const [loading, setLoading] = useState(true);
    const [isValid, setIsValid] = useState(false);

    useEffect(() => {
        verifyToken();
    }, []);

    const verifyToken = async () => {
        try {
            const token =
                localStorage.getItem("token");

            if (!token) {
                setIsValid(false);
                setLoading(false);
                return;
            }

            const response = await fetch(
                "http://localhost:5000/verify-token",
                {
                    headers: {
                        Authorization:
                            `Bearer ${token}`
                    }
                }
            );

            setIsValid(response.ok);
        } catch {
            setIsValid(false);
        }

        setLoading(false);
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    return isValid
        ? children
        : <Navigate to="/" />;
};


export default PrivateRoute;