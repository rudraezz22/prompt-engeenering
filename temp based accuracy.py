import time
import google.generativeai as genai

genai.configure(api_key = "AIzaSyAy6LCRr1_ciWQn9dmp8K19X1mbsxyXj2s")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(prompt , temp = 0.5):
    try:
        generation_config = genai.types.GenerationConfig(temperature=temp)
        response = model.generate_content(prompt , generation_config = {"temperature":temp})
        return response.text
    except Exception as e :
        print(e)

    
def stream_generate(prompt,temp=0.5):
    print("streaming_response\n")
    try:
        generation_config = genai.types.GenerationConfig(temperature=temp)
        for i in model.generate_content(prompt,generation_config = {"temperature":temp}):
            print(i.text,end ="",flush=True)

    except Exception as e:
        print(e)

def temp_activity():
    print("tempreature exploration")
    content = input("enter creative content")
    for i in [0.1,0.5,0.9]:
        print(f"tempreature is {i}")
        print(generate_response(content,i))
        time.sleep(0.5)

    topic = input("enter topic")
    instructions = [
        f"summariza key facts about {topic}",
        f"explain {topic} to a 10 year old",
        f"list the pros and cons os {topic}",
        f"create a 2050 news headline for {topic}"
    ]

    for i , instr in enumerate (instructions , 1):
        print(f"\n{i}.{instr}")
        print(generate_response(instructions,temp=0.7))
        time.sleep(.5)
    print("now its ur turn")
    instr = input("your prompt")
    try:
        tempreature = float(input("enter tempreature between 0.1-0.9"))
        if not 0.1<=tempreature <=1.0:
            raise ValueError
    except ValueError :
        print("invalid input using terreature as 0.7")
        tempreature = 0.7
    print(generate_response(instr,tempreature))

def main():
    print("gemini prompt playground!")
    print("1.explore instruction & tempreature \n 2.try streaming prompt")
    choice = int(input("enter between 1 or 2"))
    if choice == 1:
        temp_activity()
    elif choice == 2:
        prompt = input("enter ur promt")
        try:
            tempreature = float(input("enter the tempreature between 01-0.9"))
            if not 0.1<= tempreature<=1.0:
                raise ValueError
        except ValueError:
            print("invalid input using terreature as 0.7")
            tempreature = 0.7
        stream_generate(prompt,tempreature)
    else:
        print("invalid choice")

main()




    