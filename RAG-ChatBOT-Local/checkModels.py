import ollama
import pandas as pd

# Get the list of available models
models_info = ollama.list()
# print(models_info)
models = models_info.get("models", [])

# Extract relevant details
data = []
for model in models:
    name = model.get("model", "family")  # Ensure "name" exists
    name_parts = name.split(":")  # Split model name

    family = name_parts[0]  # Extract family name
    variant = name_parts[1] if len(name_parts) > 1 else "default"  # Extract variant if available
    digest = name_parts[2] if len(name_parts) > 2 else "default"

    data.append({
        "Model": model,
        "Family": family,
        "Digest": digest,
        "Format": model.get("format", "N/A"),  # Ensure "format" exists
        "Modified": model.get("modified", "N/A"),
        "Size": model.get("size", "N/A"),
    })

# Convert to Pandas DataFrame
print("\n#########################################")
print("### Available Local Ollama LLM Models ###")
print("#########################################")
df = pd.DataFrame(data)
print(df)