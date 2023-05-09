import openai

def call_gpt(prompt, api_key):      
    openai.api_key = api_key
    model_engine = 'text-davinci-003'
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
    message = completion.choices[0].text
    return message