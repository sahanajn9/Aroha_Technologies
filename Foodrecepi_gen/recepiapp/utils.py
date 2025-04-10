import requests
from django.conf import settings

def get_recipe_from_groq(ingredients):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"Generate a unique recipe using the following ingredients: {', '.join(ingredients)}. Include step-by-step instructions and a name for the dish."

    payload = {
        "model": "llama3-8b-8192",  # or "llama3-70b-8192" depending on your Groq plan
        "messages": [
            {"role": "system", "content": "You are a helpful AI chef."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"
