"""
Describe your text adventure experience.
Jude Averitt - september 2026

"""


def main() -> None:
    name: str = ""
    while name == "":
        name = input("""what do you want you character to be called? """)

    print (f""" Dear {name} 
          You have been given a mission, you have been instructed to go to the kings castle and sell the kings ceremony crown. after reading this you will have to head to the castle tonight>
          the king is planing on wearing the crown tonight at his daughter wedding do you have to retrieve it before sun set. We will come to your home tonight after sunset to retrieve the crown.
          The syndicate leader.""")
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
        You also learn that you will need to find a key for room 522. 
        You also see in the news paper today is jester additions for the kings new jester. Now you head out the the castle""")
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
    elif response in ["1", "2", "4"]:
        print("""the gards look at you and turn around and walk away as you turn around""")
        gards_kick_you_out()
    else:
          print("invalid input")
          castle_gate()
           


def make_second_decision() -> None:
    response: str = input("""You have two options now. Do you want to...
    1) go into the pipe
    2) go up to the castle gate""")
    if "1" in response:
       print("""you go though the pipe and you end up in a storage room """)
       storage_room()
    elif "2" in response:
        castle_gate()
    else:
            print("invalid input")
            make_second_decision()

def waiting_room() -> None:
    print("""you get taken in to a loud room of jesters you scan the room and see there are too exits one set of stairs to your left and a room to your right""")
    response: str = input("""wich way do you want to go?
     1) down the stairs to the left 
     2) go into the room to your right """)

    if "1" in response:
        print("you go down the stairs and you find you self in a storage room ")
        storage_room()

    elif "2" in response:
        print("you walk into the kings thron room and they think that you are next tot preform next will you try to preform or will you run away ")
        stay_or_run()

    else:
            print("invalid input")
            waiting_room()
       
def stay_or_run() -> None:
 response: str = input("""are you going got try and run or are you go to try to preform for the king?
 1) RUN
 2) Try and preform""")

 if "1" in response: 
     print("as you tun to run away the grads standing at the door grab you and take you to the front gate they throw you on and ground and close the door bright as you turn around")
     gards_kick_you_out()

 elif "2" in response: 
     print("you start trying to preform but after the king ask you to juggle and you fail the cards grads you by the shirt and throw you out of the castle as you get up ")
     gards_kick_you_out()

 else:
        print("invalid input")
        stay_or_run()


def storage_room() -> None:
   print ("""you look around and you see i bunch of boxes they are filled with all sorts of things you see cloths, tools, wood, and so on.
    on the far side of the wall there is a stair cast that says main stairs case and under that it says storage.
    now you have to decide if your going to look around the storage room or go up the stars across the room """)
   response: str = input("""do you want to go up the stars or look around the room
    1) look around the room
    2) go up the stars """)

   if "1" in response:
       looking_for_key()

   elif "2" in response:
     print("""you go up the stars and when you get to  the top you open a door and see two cards you try to close the door but the cards see you they grab you
         and take you to the kings he tells them to though you out and they take you to the Front gate and as they though you  out """)
     gards_kick_you_out()

   else:
            print("invalid input")
            storage_room()




def looking_for_key() -> None:
    print("""you look around the room you are looking though all the cloths
      when you find keys.there are two keys one key with a number 223 on it  and a key with the number 522 om it . You  have to chose one of these to keep for later""")
    response: str = input("""witch  key do you want to keep and take with you?
    1) room key 522
    2) room key 223""") 

    room_key: int = 0
    if "1" in response:
        room_key = 522 
    elif "2" in response:
        room_key = 223
    else:
        print("invalid input")
        looking_for_key()

    print("""You now walk up the stars and you find out self on landing you can here loud noises from the room next to you.
      on the wall you see it says level one. it looks like the are 6 levels you head for the stars """)

    choose_floor(room_key)


def choose_floor(room_key: int) -> None:
    
    response: str = input(""" What level do you want to go to?
    1) 1
    2) 2
    3) 3
    4) 4
    5) 5
    6) 6  """)

    if "5" in response:
        print("""you  get to the landing of level 5 and
          you see on the door kings chambers you know your in the right place you open the door and see a long hall way there 2 doors on each side.""")
        choose_door_on_level_5(room_key)
        
    elif response in ["1", "2", "4", "6"]:
        choose_floor(room_key)

    else:
            print("invalid input")
            choose_floor(room_key)

def choose_door_on_level_5(room_key: int) -> None:

    response: str = input("""What door do you want to open
    1) First door on the left 
    2) Second door on the left
    3) First door on the right
    4) Second door on the right""") 

    if "2" in response: 
      kings_room(room_key)
    elif response in ["1", "4", "3"]:
        print ("""you walk up to the door and you try to open it it is locked you try again and nothing happens
          you hear voices coming from the star well so you act fast""")
        choose_door_on_level_5(room_key)

    else:
            print("invalid input")
            choose_door_on_level_5(room_key)





def kings_room(room_key: int) -> None:

    print("""you open the door and see the kings bed. You hear noises in the hall so you jump into the room and close the door you turn around and in the corner you see it a big brown chest. 
    it's the one from the letter. you walk over to it and try to open It. It's locked you remember you you found a key from the storage room""")

    if room_key == 522:
        print("""you try the key and it works it open up and there you see it.
          you grab it and you run the the window you look out at the big drop into the mot. You take a deep breath and take a few steps back you run forward and jump!""")
        
        print("""you land in the water and swim to the edge and run home.
 latter that day you get visited by the crime syndicate leader and he takes the crown from you did it the mission is complete and you were payed 100,000 dolors and are now a well know theft.""")
        
    elif room_key == 223:

      print("""you try to open the chest but it wont bug you panic and dont know what to do you hear people walking up to the door""")
      hiding_place: str = input("where do you want to hide?")

      print(f"""you run over to the {hiding_place} and hide just as you hide you hear the door open and grades walk in. 
      They say they must be in here its the only place we have not looked.  
      You hear them say there not under where yeah not over here either then they so silent you start breaching harder then the next thing you know they pull you out""")
      print("""they bring you to the king he yells "put them in the dungeon "and you are locked behind pars for the rest of your life""")



def gards_kick_you_out() -> None:

    print("""The guards yell get out and go home you should never come back. 
    You fail""")
    


if __name__ == "__main__":
    main()