import openai


def generate_prompt(input, api_key):
    
    # Add the openai api key
    openai.api_key = api_key
    
    # Create the prompt text
    prompt_text = f"""
    You: How do I combine arrays?
    JavaScript chatbot: You can use the concat() method.
    You: {input}
    JavaScript chatbot:"""
    
    # Fetch the response from the openai API
    response = openai.Completion.create(
    engine="code-davinci-002",
    prompt=prompt_text,
    temperature=0.3,
    max_tokens=60,
    top_p=1,
    best_of=2,
    frequency_penalty=0.5,
    presence_penalty=0,
    stop=["You:"]
    )
    
    answer = response["choices"][0]["text"].strip()
    return answer