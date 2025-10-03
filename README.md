# WhatsApp Chat Analyser

A Python + Streamlit tool to analyze WhatsApp chat exports (in `.txt` format, without media) and generate insightful statistics and visualizations such as word clouds, emoji analysis, and activity timelines.

---

## 🎯 Target / Purpose

The goal of this project is to **understand communication patterns** in WhatsApp chats.  
It helps you quickly see:
- Who is most active in the conversation  
- When (time/day/month) the chat is most active  
- Which words and emojis are used most frequently  
- How overall activity trends evolve over time  

This can be useful for **personal insights**, **group activity analysis**, or even fun analytics on your friends’ and family groups.

---

## 🚀 Features

- Overall chat statistics (total messages, words, media count, links shared)  
- Timeline visualizations (daily, monthly)  
- Activity heatmap (day vs hour)  
- Word cloud & most common words  
- Emoji usage and ranking  
- User-wise filtering for group chats  
- Support for English + Hinglish stopword removal  

---

## ⚙️ Prerequisites

- Python 3.7+  
- pip  
- (Optional) A virtual environment tool (`venv`, `conda`, etc.)  

---

## 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anitripathi/whatsapp-chat-analyser.git
   cd whatsapp-chat-analyser
2. **Create and activate a virtual environment (recommended)**
   ```bash
    python3 -m venv venv
    source venv/bin/activate    # Linux/macOS  
    venv\Scripts\activate       # Windows
3. **Install dependencies***
   ```bash
       pip install -r requirements.txt

