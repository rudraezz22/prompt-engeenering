from transformers import GPT2LMHeadModel , GPT2Tokenizer

import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")


device = torch.device("cuda" if torch.cuda.is_available() else "cpu") #cuda is used for parallel processing ; this line is written to switch on cpu if gpu is not available
model.to(device)

def get_response(prompt,max_length = 50):
  inputs = tokenizer.encode(prompt , return_tensors = "pt").to(device)

  output = model.generate(
      inputs,
      max_length = max_length,
      do_sample = True, #this parameter is used that enables creative , diverse and less-predictable outputs ; if false answer will be boring
      temperature= 1.0, #to check randomness  & creativity of the text
      top_p = 0.95, #to_p is a basic decoding techique to make the text generation natural and creative
      repetition_penalty = 1.2, #it reduces repition of the content
      num_return_sequences = 1,
      pad_token_id = tokenizer.eos_token_id

  )

  response = tokenizer.decode(output[0],skip_tokens_symbol = True)
  return response

question = "what are the benefits of water?"
print(get_response(question))

command = "explain why the sky appears blue during the day scientifically"
print("\n",get_response(command))
