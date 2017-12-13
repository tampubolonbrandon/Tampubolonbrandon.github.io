print("this is an adventure! Would you like to play? (yes/no)")
response=input()
response=response.lower()

if response=='yes' or response=='y':
    print ("Great! Lets get started!")
    game = True
else:
    print("Ok, goodbye loser!")

while game==True:
    print("do you open it? (yes/no)?")
    response=input()
    response=response.lower()

    if response=='yes' or response=='y':
        print ("hissssssss.........BOOM!!!!!!")
        game = False
    else:
        print("GOOD JOB!!!!.... THERE WAS A CREEPER IN THERE")
        game = False

    print('would you like to spend 950 points? (yes/no)?')
    response=input()
    response=response.lower()

    if response=='no' or response=='n':
        print ("how are you going to defend yourself")
        game = False
    else:
        print("you got the raygun mark 2")
        game = False

    print('would you like to kill yourself? (yes/no)?')
    response=input()
    response=response.lower()

    if response=='no' or response=='n':
        print ("ok suit yourself")
        game = False
    else:
        print("you got eaten by hundreds of zombies.....WASTED")
        game = False

   
        
