---
layout: default
title: "Simple Guide to Creating Tools with OpenAI API"
date: 2023-12-15
categories: AI
---

# AI isn't just for chat! Tool creation is easy too!

When you're chatting with ChatGPT and think "Wow! This is useful! I wish I could use this for batch processing!" - it turns out it's surprisingly easy! Here's how.

Google's API and OpenAI (ChatGPT) API work similarly, but Google is free for personal use (for now), while OpenAI offers the first $5 free and then becomes paid.

---

#### 1. **Preparation**
First, complete the following preparations. Details of the procedures are abbreviated.

1. **Get API Key**  
   - Generate an API key from your OpenAI or Google account.  
   Google: https://aistudio.google.com/app/apikey
   OpenAI: https://platform.openai.com/api-keys

   - Register the obtained key in your computer's environment variables (ask AI how to do this).
   Google: Save the API key as GOOGLE_API_KEY
   OpenAI: Save the API key as OpenAI_API_KEY

2. **Install Cursor**  
   - If you know what you're doing, anything is OK. For beginners who don't know anything, install Cursor and learn from AI.

3. **Install Python**  
   - Install Python on your computer
   - Install modules for OpenAI/Google response capability (ask Cursor how to do this)

---

#### 2. **Try Using OpenAI's API**

1. **Test in Playground**  
   Access OpenAI's web tool called "Playground". Here,  
   - Select the **model you want to use** (e.g., gpt-4, etc.)
   - Set up the **desired response style** (conversation format, list format, etc.)
   Try actually chatting.

2. **Copy the Code**  
   When you find a response you like, press the "code" button on the screen to copy the Python code.

3. **Run in Cursor**  
   Paste the copied code into Cursor, save it as "test.py" or similar, and press the run button ▶! Success if no errors occur.

4. **Print the Response**  
   In the obtained code, the AI's response often isn't displayed, so you need to "add a `print()` statement to show the results" at the end. You can ask Cursor to do this.

5. **Modify as Needed**  
    For batch processing or other uses, modify with Cursor.

---

#### 3. **Google API follows the same steps!**
You can use Google's API following the same steps as OpenAI's API.
---

#### 4. **Application Examples**
By applying this, you can easily achieve things like:

- Get complex data from AI in JSON format
- Adjust responses by specifying required items and values to AI

---