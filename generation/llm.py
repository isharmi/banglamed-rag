import ollama


MODEL_NAME = "gemma3:4b"


def generate(prompt: str) -> str:
    """
    Send a prompt to the local Ollama model
    and return the generated response.
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]