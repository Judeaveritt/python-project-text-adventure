"""
Describe your text adventure experience.
Jude Averitt - september 2026

"""


def main() -> None:
    name: str = ""
    while name == "":
        name = input("""what do you want you character to be called? """)

    print("latter")
    make_first_decision()

def make_first_decision() -> None:
    response: str = input(""" what do you want to do next
    1) go to castle
    2) Research
    """)

    if "1" in response:
        castle()
    elif "2" in response:
        print("""you learn that the  kings bed is in a hallway and is the
        2rd door on the left on the 5th floor.
        you also learn that you will need to find a key for room 522. 
        your also see in the news paper today is jester additions for the kings new jester. Now you head out the the castle""")
        castle()

    else:
        print("invalid input")
        make_first_decision()



def castle() -> None:
    print("""you are at the bottom of a hill. 
    at the top is the castle and you can go up the path to the front door or walk around""")
    response: str = input("""where do you want to go?
    1) Walk around
    2) Go to the front gate
    """)

    if "1" in response:
       print("""you walk around and find a pipe in the side on of the hill.""")
       make_second_decision()

    elif "2" in response:
        castle_gate()
        
    else:
        print("invalid input")
        castle()
  
def castle_gate() -> None:
    """
    This is the 
    """
   
    response: str = input("""you walk up to the front gate a gard asks you why you are here 
    1)I want to meat the king 
    2) I am a worker to work on the castle
    3) I am here for the jester additions
    4) I am a friend of the queen""")

    if "3" in response:
        waiting_room()
    else:
        print("""the gards look at you and turn around and walk away as you turn around""")
        gards_kick_you_out()


def make_second_decision() -> None:
    response: str = input("""You have two options now. Do you want to...
    1) go into the pipe
    2) go up to the castle gate""")
    if "1" in response:
       print("""you go though the pipe and you end up in a storage room """)
       storage_room()
    elif "2" in response:
        castle_gate()

def waiting_room() -> None:
    print("""you get taken in to a loud room of jesters you scan the room and see there are too exits one set of stairs to your left and a room to your right""")
    response: str = input("""wich way do you want to go?
     1) down the sairs to the left 
     2) go into the room to your right """)

    if "1" in response:
        print("you go down the stars and you find you self in a storage room ")
        storage_room()

    elif "2" in response:
        print("you walk into the kings thron room and they think that you are next tot preform next will you try to prefrom or will you run away ")
        stay_or_run()
       
def stay_or_run() -> None:
 response: str = input("""are you goin got try and run or are you go to try to preform for the king?
 1) RUN
 2) try and preform""")

 if "1" in response: 
     print("as you tun to run away the gards stading at the door grab you and take you to the front gate they throw you on and ground and close the door bright as you turn around")
     gards_kick_you_out()

 elif "2" in response: 
     print("you start trying to preform but after the king ask you to juggle and you fail the cards grads you by the shirt and throw you out of the catle as you get up ")
     gards_kick_you_out()

#TODO: this is where i left of 
def storage_room() -> None:
   print ("""you look around and you see i bunch of boxes they are filled with all sorts of things you see cloths, tools, wood, and so on.
    on the far side of the wall there is a stair cast that says main stairs case and under that it says storage.
    now you have to decide if your going to look around the storage room or go up the stars across the room """)
   response: str = input("""do you want to go up the stars or look around the room
   """)



    












def gards_kick_you_out() -> None:
    print("""the guards yell get out and go home you should never come back. 
    You fail""")
    


if __name__ == "__main__":
    main()