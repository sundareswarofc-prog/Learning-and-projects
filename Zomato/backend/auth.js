
import jwt from "jsonwebtoken";

const auth = (req, res, next) => {
    try {
        const token =
            req.headers.authorization?.split(" ")[1];

        if (!token) {
            return res.status(401).json({
                message: "No token"
            });
        }

        const decoded = jwt.verify(
            token,
            process.env.JWT_SECRET || "zomato-secret-key"
        );

        req.user = decoded;

        next();
    } catch (err) {
        return res.status(401).json({
            message: "Token expired or invalid"
        });
    }
};

export default auth;

