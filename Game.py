### Importing Modules ###
from sys import argv, exit
from hashlib import md5



### Main Levels ###
def Route(Level, Value):

    flag = {
        "1": "b47448b1f68edd096fcf3073ac92bb11",
        "2": "1761d487ba0cde5f285059b5cca9a22c",
        "3": "a37db0ae2da5d3e7ce319340ef83e9d5",
        "4": "d44bad9f727f8bdd4da2489713660fc5",
        "5": "dbb9706700b2086cf7bd44c979e6541f",
        "6": "d065745bc7b8f84d504bb39eb419e8cd",
    }

    if Value == "info":

        print(Info(Level))

    else:

        try:
            
            if flag[Level] == str(md5(str(Value).encode()).hexdigest()):

                print("Good Job!")

            else:

                print("Try Again!")

        except:

            print("Try Again!")



### Info For Levels ###
def Info(Level):
    
    # lvl 1
    if Level == "1":

        return "Name: Dolcelino Capon \nPhone: 0320 5454624 \nCountry code: 39 \nBirthday: September 13, 1964 \nAge 23 \nJob: Vending machine repairer \nNote: His wife payed you to hack his finstagram account so you already got the username: dolcelino1964 \nHint: Getting Started..."

    # lvl 2
    elif Level == "2":

        return "Name: Ruby M. Wilson \nPhone: 079 6923 7751 \nCountry code: 44 \nBirthday: June 4, 2000 \nAge: 23 \nJob: Network Admin \nNote: try to get access to the admin account but what is the username? \nHint: Not a really dutiful network admin. Maybe lazy?"

    # lvl 3
    elif Level == "3":

        return "Name: Torsten Konig \nPhone: 04836 75 70 95 \nCountry code: 49 \nBirthday: July 19, 1989 \nAge: 34 \nJob: Account Trade \nNote: Your friend asked you to hack a scammer on stean platform to get his account back. You used your osint skills to identify your target and you relised he puts people's accounts for sale! Steal his own stean account and sell it! \nHint: warming up..."

    # lvl 4
    elif Level == "4":

        return "Note: A hacker called DEAD MOUSE hacked your personal website. You got their email from their deface page and now you want to know who are they! mouse@dead.hack \nHint: It happens sometimes. Just a bit hard but you can do it! \nPassword format is [EMAIL]:[PASSWORD]"

    # lvl 5
    elif Level == "5":

        return "Note: A person on finstagram tries to scam people with fake(Mostly Trash) home appliances... Hack their finstagram account and delete it! \nHint: You used your osint skills and the only information you got is that there is a phone number ends with 95 from Germany."

    # lvl 6
    elif Level == "6":

        return "Note: You are trying to hack a Space Research Facility to see if they got any aliens there or not. \nHint: Impossible"



# ### Hash Fuction ###
# def Hashing():

#     def HashMD5(value):

#         value = str(value).encode()
#         output = str(md5(value).hexdigest())

#         return output

#     lvl_1_ = "hidden"
#     lvl_2_ = "hidden"
#     lvl_3_ = "hidden"
#     lvl_4_ = "hidden"
#     lvl_5_ = "hidden"
#     lvl_6_ = "hidden"

#     print(f"Hash value {lvl_1_} =>", HashMD5(lvl_1_))
#     print(f"Hash value {lvl_2_} =>", HashMD5(lvl_2_))
#     print(f"Hash value {lvl_3_} =>", HashMD5(lvl_3_))
#     print(f"Hash value {lvl_4_} =>", HashMD5(lvl_4_))
#     print(f"Hash value {lvl_5_} =>", HashMD5(lvl_5_))
#     print(f"Hash value {lvl_6_} =>", HashMD5(lvl_6_))



### It's Show Time ###
if __name__ == '__main__':
    try:
        Route(argv[1], argv[2])
        # Hashing()
    except:
        print("Usage: ~$ python3 Game.py [LEVEL] [FLAG/info]")
