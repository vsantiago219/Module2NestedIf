#Task 1: Code Correction
attendees = int(input("Enter the number of attendees? \n"))
venue = ("large hall", "conference room")

venue = "large hall" if attendees > 100 else "conference room" 
print(venue)



#Task 2: Venue Selection

attendees = int(input("Enter the number of attendees? \n"))
venue = ("large hall", "conference room")

venue = "large hall" if attendees > 100 else "conference room" 
print(venue)

technology = input("Do you want any technology (yes/no): \n")

sound = "audio system" if attendees > 100 and technology == "yes" else print("projector")
print(sound)




#Task 3 Catering  Choices

vegertarian = input("Do you want vegetarian? (yes/no) \n") 

caterer = "I recommend Veggie Delight Caterers" if vegertarian == "yes" else print("I recommend Gourmet Meal Caterers") 
print(caterer)
