from openai import OpenAI

# if you saved the key under a different variable name, you can do something like:

client = OpenAI(
    api_key ="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",
)


completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a virtual assistant named jarvis skilled in genral tasks like Alexa and Google Cloud"},
        {"role": "user", "content":"what is coding"}
    ]
)
print(completion.choice[0].message.content)
 