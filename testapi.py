import openai

# Set your Hugging Face token as the API key if you use embeddings
# If you don't use embeddings, leave it empty
openai.api_key = "YOUR_HUGGING_FACE_TOKEN"  # Replace with your actual token

# Set the API base URL if needed, e.g., for a local development environment
openai.api_base = "http://localhost:1337/v1"

def main():
    chat_completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "write a poem about a tree"}],
        stream=True,
    )

    if isinstance(chat_completion, dict):
        # Not streaming
        print(chat_completion.choices[0].message.content)
    else:
        # Streaming
        for token in chat_completion:
            content = token["choices"][0]["delta"].get("content")
            if content is not None:
                print(content, end="", flush=True)

if __name__ == "__main__":
    main()