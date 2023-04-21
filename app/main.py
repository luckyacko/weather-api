import sys 
from network_service.network_service import NetworkService

def main(): 
    network_service = NetworkService()
    print("Welcome to the best weather app in the world!")
    print("here you can check the current weather in every city on the world by entering the ")
    print("name of the city")
    print("you can exit the app at any time by writing 2")
    while True:
        print("1. enter city")
        print("2. exit program")
        user_input: str =input(">> ")
        match user_input: 
            case "1":
                city =input("city: ")
                network_service.lookup_weather(city)
            case "2":
                sys.exit()
            case _:
                print("please enter a valid input")
                pass
        

    



if __name__ == "__main__":
    main()
