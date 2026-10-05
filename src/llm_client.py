import requests

class LLMClient:
    def __init__(self, url="http://127.0.0.1:11434/api/generate", model="qwen2.5:7b-instruct"):
        self.url = url
        self.model = model

    def ask(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        resp = requests.post(self.url, json=payload)
        data = resp.json()
        return data["response"]