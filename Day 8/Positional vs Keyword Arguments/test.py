# def calculate_love_score(name1, name2):
#     name=name1.lower()+name2.lower()
#     print(name)
#     print("truelove")
#
#     score1=0
#     score2=0
#     for letter in name:
#         if letter in "true":
#             score1+=1
#             print(letter + "1")
#         if letter in "love":
#             score2+=1
#             print(letter + "2")
#
#     score=str(score1)+str(score2)
#     print(f"The love score is {score}")
#
# calculate_love_score("Kanye West", "Kim Kardashian")

#--------------------------------------#
def life_in_weeks(age):
    years_left= 90-age
    weeks_left=52*years_left
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(56)