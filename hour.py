#Write a program that asks the user for an hour between 1 and 12,
#asks them to enter am or pm, and asks them how many hours into the
#future they want to go. Print out what the hour will be that many
#hours into the future,printing am or pm as appropriate.
#An example is shown below.

hour = int(input("Enter hour "))
am_pm = int(input("Enter am(1) or pm(2) "))
ahead_h = int(input("Enter how many hours ahead ?"))
if (am_pm == 1 and hour + ahead_h <=12):
    print(hour + ahead_h, " am")
elif (am_pm == 2 and hour + ahead_h <=12):
    print(hour + ahead_h, " pm")
elif (am_pm == 1 and hour+ahead_h >=12):
    print((hour + ahead_h-12), " pm")
else:
    print((hour + ahead_h-12), " am")
