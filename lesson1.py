import google.generativeai as genai

genai.configure(api_key = "AIzaSyAy6LCRr1_ciWQn9dmp8K19X1mbsxyXj2s")

def generate_response(prompt):
    
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def silly_prompt():
    print("welcome to prompt engeneering!")
    vague_prompt = input("enter a vague prompt such as (tell me about cars)")
    vague_response = generate_response(vague_prompt)
    print(f"your prompt was {vague_prompt} ,\n ai response is {vague_response}")

    specific_prompt = input("enter specific prompt , as (how ai works in self-driven cars)")
    specific_response = generate_response(specific_prompt)
    print(f"ur specific prompt was {specific_prompt}\n ai response was {specific_response}")
    
    context_prompt = input("add context ")
    context_response = generate_response(context_prompt)
    print(f"ur specific prompt was {context_prompt}\n ai response was {context_response}")

silly_prompt()

