from gen_fun import get_response

def main_bot():
    print("chatbot: Hi How can assist you Sohila?")
    
    while True:
        user_input = input("user: ").lower()
        
        if user_input == "goodbye":
            print("chatbot: See you later!")
            break
            
        response = get_response(user_input)
        print("chatbot:", response)

if __name__ == "__main__":
    main_bot()