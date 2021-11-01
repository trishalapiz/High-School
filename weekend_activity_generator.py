# based on https://onedrive.live.com/?cid=003F49AE1D3039DB&id=3F49AE1D3039DB%2185330&parId=3F49AE1D3039DB%211083&o=OneUp

import random

#winter_activities = {"reading" : 1, "eating" : 2, "tennis" : 3, "movies" : 4, "shopping" : 5, "cooking" : 6}
#summer_activities = {"reading" : 1, "eating" : 2, "tennis" : 3, "movies" : 4, "shopping" : 5, "cooking" : 6, "swimming" : 7, "kayaking" : 8}

#winter = random.randrange(1,7)
#summer = random.randrange(1,9)

#activities = {"reading" : 1, "eating" : 2, "tennis" : 3, "movies" : 4, "shopping" : 5, "cooking" : 6, "swimming" : 7, "kayaking" : 8}


"""
def getMonth(): #return an integer used to retrieve month
    try:
        current_month = int(input("What is the current month? (Please enter a number between 1 and 12) "))
        if current_month < 0 or current_month > 11:
            print("You are only allowed to enter a number within the boundary")
        elif current_month > 3 and current_month < 11:
            print("You cannot go swimming or kayaking at this time of year")
            activity = winter
            break
        else:
            print("You may go swimming or kayaking at this time of year")
            activity = summer
            break
    except ValueError:
        print("Please enter a number between 1 and 12")
"""

def generateActivities(season): # generate activities depending on season // RETURN 2 ACTIVITIES

    activities = {1 : "reading", 2 : "eating", 3 : "tennis", 4 : "movies", 5 : "shopping", 6 : "cooking", 7 : "swimming", 8 : "kayaking"}
    
    if season == "winter":
        first = random.randrange(1,7)
        second = random.randrange(1,7)
    else:
        first = random.randrange(1,9)
        second = random.randrange(1,9)

    return activities[first], activities[second]

def main():

    months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    season = ""
    
    # validate user-entered month
    while True:
        try:
            current_month = int(input("What is the current month? (Please enter a number between 1 and 12) "))
            if current_month < 1 or current_month > 12:
                print("You are only allowed to enter a number within the boundary")
            elif current_month > 4 and current_month < 12: #WINTER
                print("You cannot go swimming or kayaking at this time of year")
                season = "winter"
                break
            else:
                print("You may go swimming or kayaking at this time of year")
                season = "summer"
                break
        except ValueError:
            print("Please enter a number between 1 and 12")

    month = months[current_month]
    
    activity_one, activity_two = generateActivities(season) # season will only either be 'winter' or 'summer'

    #test valid name for user and user's friend
    name = friend_name = ""

    while True:
        try:
            name = input("What is your name? ")
            if len(name) < 3 or len(name) > 15:
                print("A valid name is between 3-15 characters long")            
            else:
                print("Hi {}".format(name))
                break
        except ValueError:
            print("Please only enter letters")
            
    while True:
        try:
            friend_name = input("What is your friend's name? ")
            if len(friend_name) < 3 or len(friend_name) > 15:
                print("A valid name is between 3-15 characters long")
            else:
                print("Hi {}".format(friend_name))
                break
        except ValueError:
            print("Please only enter letters")

    #print out the outcome
    print("*" * 60)
    print("{}, your plan for your weekend activities with your friend {} is: ".format(name, friend_name))
    print("Current month is: {}".format(month))
    print("On Saturday your activity will be: {}".format(activity_one))
    print("On Sunday your activity will be: {}".format(activity_two))    
    print("*" * 60)


main()
