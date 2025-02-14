import os
import google.generativeai as genai

genai.configure(api_key="Your api... from google AI studio")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)
def GenerateResponse(input_text):
    response = model.generate_content([
    "input: who are you ?",
    "output: I am Dharshan's chatbot Assistant",
    "input: What all can you do?",
    "output: We help people to build innovative projects",
    f"input: {input_text}",
    "output: ",
    ])
    return response.text

#while True:
    #string = str(input("Enter your prompt:"))
    #print("Bot:", GenerateResponse(string))
    
