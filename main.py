def add_habits():
    habit=input("Enter you habit: ")
    habits.append(habit)
    return habits


habits=[]
status={}
print(add_habits())