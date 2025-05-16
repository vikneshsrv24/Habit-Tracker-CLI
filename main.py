import json
import os

# Loading previous data from JSON file if exists
if os.path.exists("habits.json"):
    with open("habits.json","r") as f:
        data=json.load(f)
        habits=data.get("habits",[])
        status=data.get("status",{})
        streak=data.get("streak",{})
else:
    habits=[]
    status={}
    streak={}

# Funtion to Add habits
def add_habits():
    habit=input("Enter you habit: ")
    habits.append(habit)
    status[habit]=0
    save_data()
    print(f"{','.join(habits)} added successfully")      # to remove the brackets of the array
    morehabit=input("Do you want to include more habits(y/n) !: ")
    if morehabit =='y':
        add_habits()
   
# Function to view habits
def view_habits():
    for i in (habits):     
        print(i)

#  Create a function that can summarize the habits.
def summary():
    for j in habits:
        if status[j]==1:
            print(f" {j} is Completed ✅")
        else:
            print(f" {j} is not Completed ❌...")


#  Create a function to mark the habits that is done. 
def update_status():
    for habit in habits:
        state=input(f"Did you complete {habit} today ? (type '1' for completed or '0' for not): ")
        if state==1:
            streak[habit]=streak.get(habit,0)+1
        else:
            streak[habit]=0
        status[habit]=int(state)
<<<<<<< Updated upstream
        # if state==1:
        #     streak[habit]=streak.get(habit,0)+1
        # else:
        #     streak[habit]=0
=======
        if state==1:
            streak[habit]=streak.get(habit,0)+1
        else:
            streak[habit]=0
>>>>>>> Stashed changes
    save_data()

# Saving data into json
def save_data():
    with open("habits.json","w") as f:
        json.dump({"habits":habits,"status":status,"streak":streak},f,indent=4)

# Clear saved JSON memory
def clear_memory():
<<<<<<< Updated upstream
    habits.clear()
    status.clear()
    streak.clear()
    save_data()
    print("All Memory cleared !")
=======
    memory_clear=input("Are you sure to remove all the saved progress(Type 'y'/'n'): ")
    if memory_clear.lower()=='y':
        habits.clear()
        status.clear()
        streak.clear()
        print("All Memory cleared !")
    else:
        return
    save_data()
    

 # Edit an Habit
def edit_habit():
    print("From below which one habit you want to edit !")
    for habit in habits:
        print(habit)
    edit=int(input('Enter the habit index you want to edit: '))
    new_edit=input("Enter the name of the new habit: ").lower()
    
    old_habit=habits[edit]
    habits[edit]=new_edit

    status[new_edit]=status.pop(old_habit)
    save_data()
    print("Habit updated successfully !")

>>>>>>> Stashed changes

# View streaks
def view_streaks():
    for habit in habits:
<<<<<<< Updated upstream
        print(f"{habit} --> Streak:{streak.get(habit,0)*'🔥'}")

=======
        print(f"{habit} --> Streak:{streak.get(habit,0*'🔥')}")
>>>>>>> Stashed changes


# Main menu
streak={}
loop=1
while loop>0:
    print('\n'*1)
    print("1. Add Habits")
    print("2. View Habits")
    print("3. Update Status")   
    print("4. View Summary")
    print("5. View Streaks")
<<<<<<< Updated upstream
    print("6. Clear Saved Habits\n")        
=======
    print("6. Edit Habit")
    print("7. Clear Saved Habits\n")        
>>>>>>> Stashed changes
    option=int(input("What you wish to do ? [Type number from the options] : "))
    if option==1:
        add_habits()
    
    elif option==2:
        view_habits()
    
    elif option==3:
        update_status()

    elif option==4:
        summary()
    
    elif option==5:
        view_streaks()
<<<<<<< Updated upstream
    elif option==6:
        clear_memory()

=======
    
    elif option==6:
        edit_habit()
    
    elif option==7:
        clear_memory()
    
>>>>>>> Stashed changes
    else:
        print("Not available input. Please run again !!!")
        loop=0
        