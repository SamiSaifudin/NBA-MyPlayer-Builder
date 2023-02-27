# NBA-MyPlayer-Builder

This is a command-line application that allows users to customize their own NBA players using Python. The project includes various global variables used throughout the code that highlight specific user information such as "user_height."

## How It Works

The application starts by asking the user to pick their name and position. Then, using a class created specifically for this project called Player_base, the application creates an instance of the class for the user. This class includes the basic athleticism stats that every player has regardless of position, such as speed, strength, acceleration, and vertical. These base stats are instance variables, and there is a maximum level for each one based on the user's chosen position.

Next, the user is given the opportunity to adjust these base stats. Based on the user's responses to the prompts given, different instance methods from the Player_base object are called. These instance methods have the job of adjusting the stat the user decides they want to change and by how much the user decides to change it. These instance methods also make sure to check if the user's request is actually possible. Exception handling is used within this portion of the project to ensure the user is entering in valid answers to the prompts.

After the user has adjusted their base stats, they are prompted to choose their height. Based on the height the user chooses, changes will be made to their base stats. For example, if a user chooses a shorter height, they will see some speed/acceleration boosts and a strength decrease but if a user chooses a taller height, they will see some strength/vertical boosts and a speed/acceleration decrease.

Next, the user is prompted to pick what college they want to go to and then what NBA team they would like to go to. The user can either decide to have this randomized or pick for themselves. They also choose their jersey number, which has to follow NBA guidelines in regards to the jersey number the user picks.

Lastly, the user decides what archetype they would like to play as. An archetype is essentially a player's playstyle. Every archetype has three stats that key in on what they do best. There are a total of 7 combined archetypes (Playmaker, Sharpshooter, Shot Creator, Lockdown, Glass Cleaner, Post Scorer, Slasher), but the archetypes available to the user are based on the position they chose earlier. Using a class called Player_archetype, the application creates an instance of the class for the user. This class includes the 3 focused stats of the archetype the user chooses, which act as instance variables. The maximum level for each focused stat is 90.

The user is then given the opportunity to adjust these focused stats using different instance methods from the Player_archetype object. These instance methods have the job of adjusting the stat the user decides they want to change and by how much the user decides to change it. These instance methods also make sure to check if the user's request is actually possible. Exception handling is used within this portion of the project to ensure the user is entering in valid answers to the prompts.

Lastly, all the information regarding the user's player is printed out, completing the MyPlayer builder process.

## Concepts Used

- Object-oriented programming concepts in Python to organize code and improve code readability
- Custom classes to represent different player attributes and characteristics
- Utilized instance methods to define behavior and manipulate data within class instances.
