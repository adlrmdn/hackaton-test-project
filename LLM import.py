from ai71 import AI71 

AI71_API_KEY = "api71-api-35044c12-3e5c-47c7-ba3e-5e9d7716cc3f"

for chunk in AI71(AI71_API_KEY).chat.completions.create(
    model="tiiuae/falcon-11b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
    stream=True,
):
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, sep="", end="", flush=True)

