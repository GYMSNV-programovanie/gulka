import tkinter as tk
import random
# https://stackoverflow.com/questions/50431138/how-to-make-objects-move-smoothly-tkinter
# Create a function to draw on the canvas
root = tk.Tk()
root.title("Guľka")

x_mouse, y_mouse = 0,0
y_gulka = 20
x_gulka = 0
velkost_gulky = 50
sirka_podstavy = 100 #polomer
is_gulka = False
rychlost = 3
score = 0


def update_mouse_position(event):
    global x_mouse, y_mouse
    x_mouse, y_mouse = event.x, event.y
    canvas.delete("podstava")
    canvas.create_rectangle(x_mouse - sirka_podstavy,650,x_mouse+sirka_podstavy,680,outline ="black",fill ="white",width = 2, tags="podstava")


# def generate_gulka():
#     poloha  = random.randint(50,1300)



def gulka_pohyb():
    global x_mouse, y_mouse , x_gulka , y_gulka, velkost_gulky, is_gulka, rychlost, sirka_podstavy, score
   
    print(x_mouse)
    canvas.delete("gulka")
   
    if is_gulka == False: 
        # x_gulka = random.randint(50,1300)
        x_gulka= 200
        is_gulka = True
    else:
        canvas.create_oval(x_gulka,y_gulka, x_gulka +velkost_gulky, y_gulka + velkost_gulky,outline ="black",fill ="red",width = 2, tags="gulka")
        y_gulka += rychlost
        if y_gulka  >= (650 - velkost_gulky )  and (x_mouse - sirka_podstavy)<  x_gulka and (x_mouse + sirka_podstavy)> x_gulka:
            # rychlost += 3
            # sirka_podstavy -= 2
            score +=1
            Score_label.config(text=f"Score: {score}")
            rychlost = rychlost * (-1)
        elif y_gulka <= 0:
            rychlost = rychlost * (-1)



    

def clock():
    gulka_pohyb()
    root.after(10, clock)


# Create the main window


# Create a canvas widget
canvas = tk.Canvas(root, width=1400, height=700, bg="blue")
canvas.pack()

Score_label = tk.Label(root, text="Score: 0")
Score_label.pack()


# Create an exit button to close the application
quit_button = tk.Button(root, text="Exit", command=root.quit)
quit_button.pack()

# Bind mouse motion event to update_mouse_position
canvas.bind("<Motion>", update_mouse_position)

clock()

# Start the Tkinter main loop
root.mainloop()
