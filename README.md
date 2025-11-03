# NPC_Generator_project
Create a NPC Generator for a school project (solo)

## Highlights
Creates a certain number of NPC's depending on the user's input.

Each NPC has five different character traits including:
- Name
- Gender
- Age
- Social Status
- Height

The program also knows to choose the name of the NPC according to it's gender. Meaning that it won't give a female name like Emily if the gender chosen for that NPC is male.

All the user needs to do is enter the number of NPC's they want to generate and the program will do the rest
 
 ## Overview
This project was created to make creating NPC's for games much easier by making each NPC have it's own unique traits everytime for each one the user decides to create. The way the program selects each trait is very simple as all of the traits except age are selected by creating a list and using the random.choice command to select the trait for the NPC. The only difference with age is that is uses random.randint(1,100) to select age of the NPC ranging from 1 to 100 years old.

## Example of final product
```py
Mary 
Age: 33 
Social Class: Poor 
Height: 5.5 ft
```

## Author
I'm [Jaden Hasenfus](https://github.com/Senorpancake2) and I created this project to adding NPC's to an open world type game easier for everybody and to show that the mechanics of making a unique NPC can be fairly simple and easily recreated and looped for more NPC's. Overall, this project is meant to easily integrate an NPC generator into any type of game that you might need it for by just tampering with the varibles and attributes. 