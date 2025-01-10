from openai import OpenAI
client = OpenAI()

filename = "1"
transcript = ""
with open(f"Output/{filename}.txt","r") as file:
    transcript = file.read()

# response = client.chat.completions.create(
#     messages=[{
#         "role": "user",
#         "content": "Generate a set of medical notes with the following transcript:" + transcript,
#     }],
#     model="gpt-4o-mini",
# )

# print(response)

input_prompt ="Generate a set of medical notes with the following transcript:"

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": input_prompt + transcript,}],
    stream=True,
)


with open(f"Output/{filename}GPT.txt","w") as file:
    file.write(f"Input Prompt: {input_prompt} +\n")
    file.write("GPT Response: \n")
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            file.write(chunk.choices[0].delta.content)
            print(chunk.choices[0].delta.content, end="")

