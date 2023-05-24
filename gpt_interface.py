import json
import openai
import pdb


def get_api_key():
	f = open('constants.json')
	constants = json.load(f)
	openai.api_key = constants["openai_api_key"]
	f.close()

def call_gpt_4(prompt, model="gpt-4", verbose=False):  
	get_api_key()
	messages=[{"role": "user", "content": prompt}]    
	completion = openai.ChatCompletion.create(
	  model=model,
	  messages=[
	    {"role": "user", "content": prompt}
	  ]
	)
	response = completion.choices[0].message["content"]

	if verbose:
		print("__________________________________________________________________")
		print("Input: ", prompt)
		print("__________________________________________________________________")
		print("Output:")
		print(response)
		print("__________________________________________________________________")
	return response


prompt = "I want to create a business selling smart pools. Help me with a good business plan."

output = call_gpt_4(prompt, verbose=True)