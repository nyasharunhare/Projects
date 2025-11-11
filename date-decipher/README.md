# 💌 Date Decipher

**Date Decipher** is an interactive web-based chat app that recreates the thrill of *reading a flirty note from your crush* but with AI-powered feedback.  
As users read sweet or playful texts, the app captures their **real-time facial expressions** using the **Google Cloud Vision API**, mirrors those emotions as emojis in the chat, and finally predicts how the “crush” might feel based on those reactions.

---

## 🎯 Project Overview

Developed as my **CS50 Final Project**, Date Decipher blends web development, emotion recognition, and playful interaction design.  
It explores how technology can make digital communication more expressive and human by reading subtle emotional cues; the smiles, surprise, and blushing moments that words alone can’t convey.

---

## ✨ Core Features

- **Emotion-Aware Chat** – Captures facial expressions in real time as users read cute messages from their crush  
- **Emoji Reflection** – Displays corresponding emojis in the chat to visualize emotions (joy, surprise, neutrality, etc.)  
- **Final Feedback** – At the end of the chat, summarizes how the crush “feels about you” based on cumulative emotion data  
- **User Authentication** – Secure login and registration flow  
- **Privacy-Focused** – Clears feedback after viewing to ensure confidentiality  

---

## 🧠 How It Works

1. The user logs in and starts a chat session through a simple **Flask** interface.  
2. As they read playful “crush” messages, their webcam captures facial expressions.  
3. The **Google Cloud Vision API** analyzes each frame for emotion categories (joy, sorrow, surprise, anger, etc.).  
4. The detected emotion appears as an emoji in the chat window, making the conversation dynamic and reactive.  
5. Once the chat ends, the system analyzes the sequence of emotions and provides **final feedback** — an interpretation of how engaged or interested the crush appeared.  
6. Feedback is cleared automatically for privacy.

---

## 🧩 Technologies Used

**Languages & Frameworks:** Python, Flask, HTML, CSS, JavaScript  
**APIs:** Google Cloud Vision (for facial expression detection)  
**Libraries:** Requests, Jinja2, Bootstrap  

---

## 📺 Demo

🎥 **Video Walkthrough:** [Watch on YouTube](https://youtu.be/3Ip_VW0s-7o?si=5SVgwdZiQJDEedpV)

---

## 🌱 Reflection

This project was my first deep dive into **emotion-aware computing** — combining AI with human connection.  
It taught me how to integrate real-time facial recognition into a web app and translate emotional signals into visual, interactive experiences.  
Date Decipher reflects my fascination with the space where **data meets emotion** — and how algorithms can enhance communication rather than replace it.

---

## 🙏 Acknowledgments
- **Google Cloud Vision API** – powering real-time emotion recognition  
- **Flask Community** – for the flexible web framework  
- **CS50 Faculty & Duck Debugger** – for foundational support and inspiration  
- **OpenAI’s ChatGPT** – for debugging and documentation assistance  

---

