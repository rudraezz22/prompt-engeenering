import os 
from google import genai
from google.genai import types

gemini_api_key = ("AIzaSyAy6LCRr1_ciWQn9dmp8K19X1mbsxyXj2s")

client = genai.Client(api_key = gemini_api_key)

def generate_response(prompt,tempreature = 0.3):
  try:
    contents = [types.Content(role = "user" ,  parts = [types.Part.from_text(text = prompt)])]
    config = types.GenerateContentConfig(temperature = tempreature)
    response = client.models.generate_content(model = "gemini-2.0-flash" , contents = contents , config = config )
    return response.text
  except Exception as e:
    return f"the error is {e}"

def rl_learning():
  print("WELCOME! to reinforcement based larning ! \n")
  prompt = input("enter ur prompt (e.g describe a lion)")
  initial_response = generate_response(prompt)
  print(f"the initial response is {initial_response}")

  rating = int(input("\n enter rating between 1-5"))
  feedback = input("\n enter feedback\n")
  improved_response = f"initial response {initial_response}  improved with ur feedback { feedback}"

  print(f"\n ur new response is {improved_response}")


def role_based_activity():
  print("WELCOME! to role based larning !")
  category = input("enter u category (e.g science , math , history)")
  item = input(f"enter specific category {category}")

  te_prompt = input("1.teacher , 2. expert")
  if te_prompt == "1":
    teacher_response = generate_response(item)
    print(f"Teacher's reponse is {teacher_response}")
  
  elif te_prompt == "2":
    expert_response = generate_response(item)
    
    print(f"expert bsed reponse is {expert_response}")
  

def main():
  response_choice = input("enter ur choice : 1.reinforced learning , 2.role_based_activity")

  if response_choice == "1":
    rl_learning()
  elif response_choice == "2":
    role_based_activity()
  else:
    print("invalid input enter a valid input ")

main()
