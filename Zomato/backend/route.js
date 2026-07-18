import express from "express";
const router = express.Router();
import bcrypt from "bcrypt";
import pool from "./pgConfig.js";
import jwt from "jsonwebtoken";
import auth from "./auth.js";
import nodemailer from "nodemailer";
import dotenv from "dotenv";


const transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
        user: process.env.GMAIL,
        pass: process.env.PASSWORD
    }
});

const otpStore = {};


router.post("/signup", async (req, res) => {
    console.log(req)
    try {
        const { fullName, email, password } = req.body;
        if (fullName && email && password) {
            const hashedPassword = await bcrypt.hash(password, 10);

            const existingUser = await pool.query(
                "SELECT * FROM users WHERE email = $1",
                [email]
            );

            if (existingUser.rows.length > 0) {
                return res.status(400).json({
                    success: false,
                    message: "Email already exists"
                });
            }

            const result = await pool.query(`
      INSERT INTO users
      (fullname, email, password)
      VALUES ($1, $2, $3)
      RETURNING *
      `,
                [fullName, email, hashedPassword]
            );

            const token = jwt.sign(
                {
                    id: result.rows[0].id,
                    email: result.rows[0].email
                },
                process.env.JWT_SECRET || "zomato-secret-key",
                {
                    expiresIn: "1d"
                }
            );



            res.status(200).json({
                success: true,
                user: result.rows[0],
                token
            });
        }

    } catch (err) {
        res.status(500).json({
            success: false,
            message: "Server Error",
        });
    }
});

router.post("/login", async (req, res) => {

    const { email, password } = req.body;
    try {
        if (email && password) {

            const result = await pool.query(
                "SELECT * FROM users WHERE email = $1",
                [email]
            );


            if (result.rows.length === 0) {
                return res.status(404).json({
                    message: "User not found",
                });
            }
            const user = result.rows[0];
            const isPasswordMatch = await bcrypt.compare(
                password,
                user.password
            );

            if (!isPasswordMatch) {
                return res.status(401).json({
                    message: "Invalid password",
                });
            }


            const otp = Math.floor(100000 + Math.random() * 900000);

            otpStore[email] = {
                otp,
                expiresAt: Date.now() + 5 * 60 * 1000
            };

            await transporter.sendMail({
                from: process.env.EMAIL,
                to: email,
                subject: "OTP Verification",
                text: `Your OTP is ${otp}`
            });

            return res.status(200).json({
                message: "OTP sent successfully",
            });

        }
        else {

            const otp = Math.floor(100000 + Math.random() * 900000);
            delete otpStore[email];

            otpStore[email] = {
                otp,
                expiresAt: Date.now() + 5 * 60 * 1000
            };

            console.log(otpStore, "otpStore")

            transporter.sendMail({
                from: process.env.EMAIL,
                to: email,
                subject: "OTP Verification",
                text: `Your OTP is ${otp}`
            });

            return res.status(200).json({
                message: "OTP sent successfully"
            });
        }
    }

    catch (err) {
        console.error(err);
        return res.status(500).json({
            message: "Server Error"
        });
    }


});

router.get("/foodlist", async (req, res) => {
    try {
        const result = await pool.query(
            `SELECT
            f.*,
            c.category_name,
            r.name AS restaurant_name,
            r.rating AS restaurant_rating,
            r.address AS hotel_address
        FROM food_items f
        JOIN categories c ON f.category_id = c.id
        JOIN restaurants r ON f.restaurant_id = r.id;`
        );
        if (result.rows.length === 0) {
            return res.status(404).json({
                message: "food items not found",
            });
        }

        if (result.rows.length) {
            res.status(200).json(result.rows)
        }
    }
    catch (err) {
        console.error(err);
        res.status(500).json({
            message: "Internal server error"
        });
    }
})

router.post("/likeditems", async (req, res) => {
    const { id } = req.body
    try {
        const result = await pool.query(
            ` UPDATE food_items
            SET isLiked = NOT isLiked
            WHERE id = $1
            RETURNING *`,
            [id]
        )
        res.status(201).json({
            success: true,
            user: result.rows[0],
        });
    }
    catch (err) {
        console.error(err);

        res.status(500).json({
            success: false,
            message: "Server Error",
        });
    }
})

router.get("/verify-token", auth,
    (req, res) => {
        res.status(200).json({
            valid: true
        });
    }
);

router.post("/cartedItems", async (req, res) => {
    const { id } = req.body
    try {
        const result = await pool.query(
            ` UPDATE food_items
            SET isCart = NOT isCart
            WHERE id = $1
            RETURNING *`,
            [id]
        )
        res.status(201).json({
            success: true,
            user: result.rows[0],
        });
    }
    catch (err) {
        console.error(err);

        res.status(500).json({
            success: false,
            message: "Server Error",
        });
    }
})

router.post("/verify-otp", async (req, res) => {
    console.log(req.body, otpStore)

    try {
        const { email, otp } = req.body;


        const savedOtp = otpStore[email];

        if (!savedOtp) {
            return res.status(400).json({
                message: "OTP not found"
            });
        }

        if (Date.now() > savedOtp.expiresAt) {
            delete otpStore[email];

            return res.status(400).json({
                message: "OTP expired"
            });
        }

        if (Number(otp) !== savedOtp.otp) {
            return res.status(400).json({
                message: "Invalid OTP"
            });
        }

        delete otpStore[email];

        const result = await pool.query(
            "SELECT * FROM users WHERE email = $1",
            [email]
        );

        const user = result.rows[0];

        const token = jwt.sign(
            {
                id: user.id,
                email: user.email
            },
            process.env.JWT_SECRET || "zomato-secret-key",
            {
                expiresIn: "1d"
            }
        );

        return res.status(200).json({
            message: "Login successful",
            token,
            user: {
                id: user.id,
                fullname: user.fullname,
                email: user.email
            }
        });

    } catch (err) {
        console.error(err);

        return res.status(500).json({
            message: "Server Error"
        });
    }
});

export default router;