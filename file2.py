sai_details_canara = {
    "name" : "lokesh",   
    "adr" : "123 Main St",
    "pan" : "ABCDE1234F",
    "atmpin" : "12345",
}
all_attempts = 3
while all_attempts > 0:
    user_input = input("Enter your  atm pin number: ")
    if user_input == sai_details_canara["atmpin"]:
        print("pin number is correct!")
        break
    else:
        all_attempts -= 1
        print("Incorrect ATM pin number. Attempts left:", all_attempts)
    