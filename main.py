# Funtion to Add habits
def add_habits():
    habit=input("Enter you habit: ")
    habits.append(habit)
    print(f"{','.join(habits)} added successfully")      # to remove the brackets of the array
    morehabit=input("Do you want to include more habits !: ")
    if morehabit =='y':
        add_habits()
    else:
        return

# Function to view habits
def view_habits():
    for i in (habits):     
        print(i)

# TODO : Create a function that can summarize the habits.
def summary():
    for j in habits:
        if status[j]==1:
            print(f" {j} is Completed ✅")
        else:
            print(f" {j} is not Completed ❌...")



# TODO : Create a function to mark the habits that is done. 
def update_status():
    for habit in habits:
        state=input(f"Did you complete {habit} today ? (type '1' for completed or '0' for not): ")
        status[habit]=int(state)

status={}

# Main menu
habits=[]
loop=1
while loop>0:
    print('\n'*1)
    print("1. Add Habits")
    print("2. View Habits")
    print("3. Update Status")   
    print("4. View Summary\n")        
    option=int(input("What you wish to do ? [Type number from the options] : "))
    if option==1:
        add_habits()
    
    elif option==2:
        view_habits()
    
    elif option==3:
        update_status()

    elif option==4:
        summary()
    
    else:
        print("Not available input. Please run again !!!")
        loop=0
        