import os
from google import genai
from google.genai import types

gemini_api_key = "AIzaSyAy6LCRr1_ciWQn9dmp8K19X1mbsxyXj2s"

client = genai.Client(api_key = gemini_api_key)

def generate_response(prompt,temperature = 0.3):
  try:
    contents = [types.Content(role = "user" , parts = [types.Part.from_text(text = prompt)])]
    config_params = types.GenerateContentConfig(temperature = temperature )
    response = client.models.generate_content(model = "gemini-2.0-flash" , contents = contents, config = config_params)
    return response.text

  except Exception as e:
    return f"the error is {e}"

def bias_mitigation_activity():
  print("WELCOME! to bias activity")
  bias_input = input("enter a prompt to explore bias (eg. describe ideal doctor)")
  bias_response = generate_response(bias_input)

  print(f"\n initial ai response is {bias_response}")

  modified_bias = input("enter modified prompt")
  modified_response = generate_response(modified_bias)
  print(f"the modified response is {modified_response}")

def token_time_limit():
  print("WLCOME! TO TOKEN TIME ACTIVITY")
  long_prompt = input("enter a long prompt (more than 300 characters , eg. write a detailed story on ideal doctor)")
  long_response = generate_response(long_prompt)
  print(f"long detailed respons is {long_response[:2000]}")

  short_prompt = input("enter a condensed prompt to be more concised ")
  short_response = generate_response(short_prompt)
  print(f"\n condensed response is {short_response[:300]}")

def main():
  choice = input("enter choice 1. bias mititgation , 2. token_limit_activity")

  if choice == "1":
    bias_mitigation_activity()
  elif choice == "2":
    token_time_limit()
  else:
    print("not a valid choice")

main()
