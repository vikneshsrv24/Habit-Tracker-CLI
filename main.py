def add_habits():
    habit=input("Enter you habit: ")
    habits.append(habit)
    return habits

def view_habits():
    print(habits)


habits=[]
status={}
#print(add_habits())
loop=1
while loop>0:
    print(" 1.Add Habits" \
    " 2.View Habits" \
    " 3.Summary")
    option=int(input("What you wish to do [select from the options] ?"))
    if option==1:
        add_habits()
    elif option==2:
        print(view_habits())
    else:
        print(" Summary function")
        loop=0