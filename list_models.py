import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="YOUR_API_KEY")

# List models
models = genai.list_models()
for model in models:
    print(model.name, "-", model.supported_generation_methods)
