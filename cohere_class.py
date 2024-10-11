import cohere
import json

class CohereGenerator:
    def __init__(self):
        self.co = cohere.ClientV2("<TU_TOKEN>")

    def ask(self, string, model="command-r-plus", max_tokens=200):

        response = self.co.chat(
            model=model,
            max_tokens=max_tokens,
            messages = [
            {
                "role": "user",
                "content": string
            }
            ]
        )

        ditc = json.loads(response.json())
        return (ditc['message']['content'][0]['text'])