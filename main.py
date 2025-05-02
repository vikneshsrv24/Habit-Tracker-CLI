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

# TODO : Remove none type from the loop.
def view_habits():
    for i in (habits):     
        print(i)

# TODO : Create a function that can summarize the habits.
# TODO : Create a function to mark the habits that is done. 
habits_type = {

}
 
habits=[]
status={}
loop=1
while loop>0:
    print("1. Add Habits")
    print("2. View Habits")
    print("3.Checklist")   
    print("4. View Summary")        
    option=int(input("What you wish to do ? [select from the options] : "))
    if option==1:
        add_habits()
    elif option==2:
        view_habits()
    elif option==3:
        for i in habits:
            print("Type '1' if the habit is completed or '0' for pending list ")
            history=print(i).int(input(' : Completed or Pending : '))
            # if history ==1:
            #     status+=i
            # else:
    else:
        print("Not available input. Please run again !!!")
        loop=0