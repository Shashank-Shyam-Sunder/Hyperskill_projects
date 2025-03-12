#%%
import random
no_friends = int(input("Enter the number of friends joining (including you):"))

if no_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(no_friends):
        friend = input().strip()
        if friend not in friends:
            friends[friend] = 0

    total_bill = float(input("Enter the total bill value:"))
    split_amount = round(total_bill / no_friends,2)
    friends = {friend: split_amount for friend in friends}
    lucky_draw = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if lucky_draw == 'Yes':
        lucky_person = random.choice(list(friends.keys()))
        print(f"{lucky_person} is the lucky one!")
        split_amount_new = round(total_bill / (no_friends-1),2)
        for friend in friends:
            if friend == lucky_person:
                friends[friend] = 0
            else:
                friends[friend] = split_amount_new
        print(friends)

    elif lucky_draw == 'No':
        print("No one is going to be lucky")
        print(friends)

