import json

with open("data.json", "r") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
    
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return intent["responses"][0]
                
    return "Could you please rephrase that?"