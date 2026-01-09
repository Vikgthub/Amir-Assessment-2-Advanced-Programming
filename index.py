

# -----------------------------------------------------------------------------------------------------------------



# first import modules for tools and the GUI setups
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO











# -----------------------------------------------------------------------------------------------------------------



# create a color palet (I chose yellow and red to emphasize that its a dish recepie app, along with a dark back ground)
C1 = "#FF5B5B" # red
C2 = "#FFD086" # amber
C3 = "#737373" # gray
BG = "#000000" # black (background)
WH = "#FFFFFF" # white











# -----------------------------------------------------------------------------------------------------------------

# setup the screensize and give the GUI app a title
root = tk.Tk()
root.title("Meal.it")
root.geometry("950x520")
root.configure(bg=BG)














# -----------------------------------------------------------------------------------------------------------------


# create pages 
home_frame = tk.Frame(root, bg=BG, width=950, height=520) #home page
menu_frame = tk.Frame(root, bg=BG, width=950, height=520) #menu page
dish_frame = tk.Frame(root, bg=BG, width=950, height=520) #dish page












# -----------------------------------------------------------------------------------------------------------------

# define functions


def go_to_home(): # here, make a function to take user to home pagw
    #menu and dish pages are hidden and wont be showns
    menu_frame.place_forget() 
    dish_frame.place_forget()
    #user will be in home page
    home_frame.place(x=0, y=0)







def go_to_menu(): #similarly, in this function, home page and dish page wont be seen here
    #instead user will view the menu page
    home_frame.place_forget()
    dish_frame.place_forget()
    menu_frame.place(x=0, y=0)







def go_to_dish():
    #again similarly, home and menu page wont be shown, instead user is in dish page
    home_frame.place_forget()
    menu_frame.place_forget()
    dish_frame.place(x=0, y=0)










#make function to get the name of the dish
def get_meal_by_name():
    #in meal entry 
    name = meal_entry.get()
    if not name: #if name is not given
        #then return a warning and ask user to enter the name of the dish
        messagebox.showwarning("Input Error", "Please enter a meal name!")
        return
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}"
    try: #with the help of exception handling 
        #send request and convert the response into python dictionary
        data = requests.get(url).json()
        if data["meals"]: #if the name iof the meal is found 
            #then pass the first meal object in the list as an argument to the display function
            display_the_meal(data["meals"][0]) 
        else: #otherwise give an error message
            messagebox.showerror("Error", "No recipes found!")
    except: #catch errors to not close the page (beacuse of erros)
        messagebox.showerror("Network Error", "Check your connection!")





#define a function to display to user a random mean from the "themealdb" database 
def get_random_meal():
    url = "https://www.themealdb.com/api/json/v1/1/random.php" #url to the database 
    data = requests.get(url).json()#send a request to the url (the request is then converted to a python dictionary)
    display_the_meal(data["meals"][0]) #pass the first meal in the list to another function









#define a dunction to display the meals
def display_the_meal(meal):
    dish_title.config(text=meal["strMeal"].upper()) #capitalize the name of the dish
    #combine the categories, regions, and instructions 
    info = f"CATEGORY: {meal['strCategory']}\nREGION: {meal['strArea']}\n\n{meal['strInstructions']}"
    recipe_text.config(state="normal") #unlock the text box so program can write new recipe insids it
    recipe_text.delete("1.0", tk.END) #clears/deletes the text box so the previous recipe is gone
    recipe_text.insert(tk.END, info) #attach the new instruction into the text box
    #lock the text box so the user doesnt accidentally alter the recipe in the textbox
    recipe_text.config(state="disabled") 




    #now get the images from the url
    img_data = requests.get(meal["strMealThumb"]).content
    #use bytesiO to treat the imge like a file and resize it 
    img = Image.open(BytesIO(img_data)).resize((500, 500), Image.Resampling.LANCZOS)
    global final_img #dont delete the image from memory
    final_img = ImageTk.PhotoImage(img) #convert the image into a format that tkinter displays
    dish_image_label.config(image=final_img) #put the final image onto the label in the dish page 
    go_to_dish() #change the screen to the dish page 



















# -----------------------------------------------------------------------------------------------------------------




#finally create the GUI setup




#the home page

#create the logo (here I have individually put the letters to create my logo and added 2 different colors to show to show the "meal it" text and the hidden message in it "eat" )
tk.Label(home_frame, text="M", font=("Helvetica", 128, "bold"), fg=C2, bg=BG).place(x=292, y=0)
tk.Label(home_frame, text="E", font=("Helvetica", 128, "bold"), fg=C1, bg=BG).place(x=410, y=0)
tk.Label(home_frame, text="A", font=("Helvetica", 128, "bold"), fg=C1, bg=BG).place(x=489, y=0)
tk.Label(home_frame, text="L", font=("Helvetica", 128, "bold"), fg=C2, bg=BG).place(x=585, y=0)
tk.Label(home_frame, text="I", font=("Helvetica", 128, "bold"), fg=C2, bg=BG).place(x=458, y=124)
tk.Label(home_frame, text="T", font=("Helvetica", 128, "bold"), fg=C1, bg=BG).place(x=494, y=124)

#create the button to to explore te dishes in the menu page
tk.Button(home_frame, text="EXPLORE OUR DISHES", font=("Helvetica", 36, "bold"),  width=20,  fg=WH, bg=BG, highlightthickness=2, highlightbackground=WH, relief="flat", command=go_to_menu).place(x=230, y=300)

#add additional text (in this case, to show that the company is incorperated)
tk.Label(home_frame, text="Meal It ©2026", font=("Helvetica", 20), fg=WH, bg=BG).place(x=406, y=470)









#the menu page


#add text to show tat this is the menu page and to ask the user what they want 
tk.Label(menu_frame, text="MENU", font=("Helvetica", 64, "bold"), fg=WH, bg=BG).place(x=379, y=26)
tk.Label(menu_frame, text="WHAT ARE YOU LOOKING FOR?", font=("Helvetica", 30, "bold"), fg=WH, bg=BG).place(x=197, y=141)

#add entry text box to allow user to search for an item
meal_entry = tk.Entry(menu_frame, font=("Helvetica", 36), width=18, bg=C3, fg=WH, bd=0)
meal_entry.place(x=254, y=209)

#add button to allow user to search for an item
tk.Button(menu_frame, text="SEARCH", font=("Helvetica", 36), fg=C2, bg=BG, highlightthickness=1, 
          highlightbackground=C2, width=10, command=get_meal_by_name).place(x=327, y=271)

#or let the user randomly gwt a dish
tk.Button(menu_frame, text="A SURPRISE!", font=("Helvetica", 36), fg=C1, bg=BG, highlightthickness=1, 
          highlightbackground=C1, width=10, command=get_random_meal).place(x=327, y=416)
















#the dish page

#in the dish page allow user to go back to menu page
tk.Button(dish_frame, text="BACK", font=("Helvetica", 36, "bold"), fg=C1, bg=BG, 
          highlightthickness=1, highlightbackground=C1, command=go_to_menu).place(x=34, y=41)

#show the image of the dish
dish_image_label = tk.Label(dish_frame, bg=C3, width=280, height=280) 
dish_image_label.place(x=89, y=151)


#add a vertical line for separation and aesthetics 
tk.Frame(dish_frame, bg=WH, width=2, height=348).place(x=475, y=118)

#display the dish name 
dish_title = tk.Label(dish_frame, text="DISH", font=("Helvetica", 20, "bold"), fg=C2, bg=BG)
dish_title.place(x=674, y=135, anchor="center")

#and display the dish information 
recipe_text = tk.Text(dish_frame, wrap="word", width=30, height=8, font=("Arial", 14), bg=C3, fg=WH, bd=0, padx=20, pady=20)
recipe_text.place(x=580, y=260)














#end the loop
go_to_home()
root.mainloop()
