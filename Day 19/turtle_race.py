import turtle
from turtle import Turtle, Screen
import random

# Variabilă de control pentru a porni/opri bucla principală a jocului
is_race_on = False

# Configurarea ferestrei de joc (Canvas)
screen = Screen()
# Setăm dimensiunea ferestrei: 500 pixeli lățime, 400 pixeli înălțime
screen.setup(width=500, height=400)

# Apare o fereastră pop-up care cere input de la utilizator (culoarea aleasă)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Liste pentru a stoca culorile, pozițiile pe axa Y și obiectele de tip Turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Buclă pentru a crea cele 6 țestoase
for turtle_index in range(0, 6):
    # Cream o nouă instanță (obiect) a clasei Turtle
    new_turtle = Turtle(shape="turtle")
    # Setăm culoarea folosind lista definită mai sus și indexul curent
    new_turtle.color(colors[turtle_index])
    # Ridicăm "creionul" ca să nu lase urme pe ecran când se deplasează
    new_turtle.penup()
    # Mutăm țestoasa la linia de start (X este constant în stânga, Y variază)
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # Adăugăm obiectul creat în lista all_turtles pentru a-l accesa mai târziu
    all_turtles.append(new_turtle)

# Dacă utilizatorul a introdus o valoare (nu a apăsat Cancel), cursa poate începe
if user_bet:
    is_race_on = True

# Bucla principală a cursei
while is_race_on:
    for turtle in all_turtles:
        # Verificăm dacă țestoasa curentă a trecut linia de sosire (X > 230)
        # 250 e marginea, dar scădem jumătate din dimensiunea țestoasei pentru precizie
        if turtle.xcor() > 230:
            is_race_on = False  # Oprim cursa
            winning_color = turtle.pencolor()  # Aflăm culoarea câștigătorului

            # Comparăm culoarea câștigătoare cu pariul utilizatorului
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Fiecare țestoasă se mișcă cu o distanță aleatorie între 0 și 10 pixeli
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Permite închiderea ferestrei doar la un click pe ea, după finalizarea cursei
screen.exitonclick()