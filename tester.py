import openai
openai.api_key = "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"
prompt = "Hello, World!"
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  temperature=0.5,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
