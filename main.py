from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

system_assisted_prompt = """

"""

prompt = """
Type prompt into here
"""

response = client.chat.completions.create(
    model="qwen3",
    messages=[{"role": "system", "content" : ""}, {"role": "user", "content": "Hello"}],
)

print(response.choices[0].message.content)
