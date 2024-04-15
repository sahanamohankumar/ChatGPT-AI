import openai

api_key = "(enter your API key)"
openai.api_key = api_key


def generate_response(prompt):
  response = openai.Completion.create(
      engine="text-davinci-002",  # Choose the GPT-3 engine
      prompt=prompt,
      max_tokens=50  # Maximum length of the generated response
  )
  return response.choices[0].text


# Example usage
user_input = "Tell me a joke."
response = generate_response(user_input)
print(response)
