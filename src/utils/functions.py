def get_user_input() -> str:
    try:
        message = str(input("Ingresa un texto para ser analizado: "))
        return message
    except ValueError:print("You must enter a string")