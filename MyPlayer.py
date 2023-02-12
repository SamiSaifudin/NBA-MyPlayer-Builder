from time import sleep 
import random 

user_name = ""
user_height = ""
user_position = ""
user_team = ""
user_jersey_number = ""
user_archetype = ""
user_college = ""
my_player = ""
my_player_arch = ""

class Player_base:
    """
    - Player class that holds the attributes of the users created players
    - The attributes in this case refer to base athleticism stats
    - Based on users choice on position (located in position() function), attributes (max levels) vary
    - Holds methods to adjust these base stats
    - Methods are called based on user input
    - Methods check to see if user request is possible
    """
    def __init__(self):
        if user_position.upper() == "PG" or user_position.upper() == "POINT GUARD":
            self.position = "Point Guard"
            self.speed = 0
            self.strength = 0
            self.acceleration = 0
            self.vertical = 0
            self.speed_max = 85
            self.strength_max = 35
            self.acceleration_max = 70
            self.vertical_max = 66
            self.attr_points = 0 
        elif user_position.upper() == "SG" or user_position.upper() == "SHOOTING GUARD":
            self.position = "Shooting Guard"
            self.speed = 0
            self.strength = 0
            self.acceleration = 0
            self.vertical = 0
            self.speed_max = 80
            self.strength_max = 40
            self.acceleration_max = 66
            self.vertical_max = 70 
            self.attr_points = 0 
        elif user_position.upper() == "SF" or user_position.upper() == "SMALL FORWARD":
            self.position = "Small Forward"
            self.speed = 0
            self.strength = 0
            self.acceleration = 0
            self.vertical = 0
            self.speed_max = 75
            self.strength_max = 50
            self.acceleration_max = 60
            self.vertical_max = 71
            self.attr_points = 0 
        elif user_position.upper() == "PF" or user_position.upper() == "POWER FORWARD":
            self.position = "Power Forward"
            self.speed = 0
            self.strength = 0
            self.acceleration = 0
            self.vertical = 0
            self.speed_max = 65
            self.strength_max = 80
            self.acceleration_max = 50
            self.vertical_max = 61
            self.attr_points = 0 
        elif user_position.upper() == "C" or user_position.upper() == "CENTER":
            self.position = "Center"
            self.speed = 0
            self.strength = 0
            self.acceleration = 0
            self.vertical = 0
            self.speed_max = 55
            self.strength_max = 90
            self.acceleration_max = 45
            self.vertical_max = 66
            self.attr_points = 0 
    
    def speed_change(self, change_type, value_change):
        if change_type == "I":
            if (self.speed + value_change) > self.speed_max:
                print(f"Cannot do this action as it would lead to you going over the max speed level ({self.speed_max}).\n")
                sleep(2.0)
            elif (self.speed + value_change) < 0:
                print("Cannot do this action as it would lead to speed being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 230:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.speed += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.speed - value_change) > self.speed_max:
                print(f"Cannot do this action as it would lead to you going over the max speed level ({self.speed_max}).\n")
                sleep(2.0)
            elif (self.speed - value_change) < 0:
                print("Cannot do this action as it would lead to speed being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 230:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.speed -= value_change 
                self.attr_points -= value_change

    def strength_change(self, change_type, value_change):
        if change_type == "I":
            if (self.strength + value_change) > self.strength_max:
                print(f"Cannot do this action as it would lead to you going over the max strength level ({self.strength_max}).\n")
                sleep(2.0)
            elif (self.strength + value_change) < 0:
                print("Cannot do this action as it would lead to strength being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 230:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.strength += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.strength - value_change) > self.strength_max:
                print(f"Cannot do this action as it would lead to you going over the max strength level ({self.strength_max}).\n")
                sleep(2.0)
            elif (self.strength - value_change) < 0:
                print("Cannot do this action as it would lead to strength being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 230:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.strength -= value_change 
                self.attr_points -= value_change
    
    def acceleration_change(self, change_type, value_change):
        if change_type == "I":
            if (self.acceleration + value_change) > self.acceleration_max:
                print(f"Cannot do this action as it would lead to you going over the max acceleration level ({self.acceleration_max}).\n")
                sleep(2.0)
            elif (self.acceleration + value_change) < 0:
                print("Cannot do this action as it would lead to acceleration being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 230:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Point being negative.\n")
                sleep(2.0)
            else:
                self.acceleration += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.acceleration - value_change) > self.acceleration_max:
                print(f"Cannot do this action as it would lead to you going over the max acceleration level ({self.acceleration_max}).\n")
                sleep(2.0)
            elif (self.acceleration - value_change) < 0:
                print("Cannot do this action as it would lead to acceleration being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 230:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.acceleration -= value_change
                self.attr_points -= value_change
    
    def vertical_change(self, change_type, value_change):
        if change_type == "I":
            if (self.vertical + value_change) > self.vertical_max:
                print(f"Cannot do this action as it would lead to you going over the max vertical level ({self.vertical_max}).\n")
                sleep(2.0)
            elif (self.vertical + value_change) < 0:
                print("Cannot do this action as it would lead to vertical being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 230:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.vertical += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.vertical - value_change) > self.vertical_max:
                print(f"Cannot do this action as it would lead to you going over the max vertical level ({self.vertical_max}).\n")
                sleep(2.0)
            elif (self.vertical - value_change) < 0:
                print("Cannot do this action as it would lead to vertical being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 230:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.vertical -= value_change
                self.attr_points -= value_change
    
    def stat_status(self, attribute):
        if attribute == "SPEED":
            return f"Speed Current Level: {self.speed}, Speed Max Level: {self.speed_max}"
        elif attribute == "STRENGTH":
            return f"Strength Current Level: {self.strength}, Strength Max Level: {self.strength_max}"
        elif attribute == "VERTICAL":
            return f"Vertical Current Level: {self.vertical}, Vertical Max Level: {self.vertical_max}"
        elif attribute == "ACCELERATION":
            return f"Acceleration Current Level: {self.acceleration}, Acceleration Max Level: {self.acceleration_max}"

    def __str__(self):
        return f"Position: {self.position}\nSpeed: {self.speed}\nStrength: {self.strength}\nAcceleration: {self.acceleration}\nVertical: {self.vertical}\n" 
    
    def print_maxes(self):
        print(f"Speed: {self.speed_max}\nStrength: {self.strength_max}\nAcceleration: {self.acceleration_max}\nVertical: {self.vertical_max}\n")

class Player_archetype:
    """
    - Player class that holds the attributes of the users created players
    - The attributes in this case refer to focused stats based on the user's archetype
    - Based on users choice on archetype (located in pick_archetype() function), attributes (max levels) vary
    - Holds methods to adjust these focused stats
    - Methods are called based on user input
    - Methods check to see if user request is possible
    """
    def __init__(self):
        if user_archetype.upper() == "PLAYMAKER" or user_archetype.upper() == "PLAY MAKER":
            self.archetype = "Playmaker"
            self.pass_accuracy = 0
            self.ball_handle = 0
            self.speed_with_ball = 0
            self.pass_accuracy_max = 90
            self.ball_handle_max = 90
            self.speed_with_ball_max = 90 
            self.attr_points = 0 
        elif user_archetype.upper() == "SLASHER":
            self.archetype = "Slasher"
            self.driving_layup = 0
            self.driving_dunk = 0
            self.standing_dunk = 0
            self.driving_layup_max = 90
            self.driving_dunk_max = 90
            self.standing_dunk_max = 90
            self.attr_points = 0 
        elif user_archetype.upper() == "SHOT CREATOR" or user_archetype.upper() == "SHOTCREATOR":
            self.archetype = "Shot Creator"
            self.contested_shot = 0
            self.off_dribble_shot = 0
            self.post_fadeaway = 0
            self.contested_shot_max = 90
            self.off_dribble_shot_max = 90
            self.post_fadeaway_max = 90 
            self.attr_points = 0
        elif user_archetype.upper() == "SHARP SHOOTER" or user_archetype.upper() == "SHARPSHOOTER":
            self.archetype = "Sharpshooter"
            self.mid_range = 0
            self.three_point = 0
            self.free_throw = 0
            self.mid_range_max = 90
            self.three_point_max = 90
            self.free_throw_max = 90 
            self.attr_points = 0
        elif user_archetype.upper() == "LOCKDOWN" or user_archetype.upper() == "LOCK DOWN":
            if my_player.position == "Center" or my_player.position == "Power Forward" or my_player.position == "Small Forward": 
                self.archetype = "Lockdown"
                self.block = 0
                self.steal = 0
                self.interior_defense = 0
                self.block_max = 90
                self.steal_max = 90
                self.interior_defense_max = 90 
                self.attr_points = 0
            else:
                self.archetype = "Lockdown"
                self.block = 0
                self.steal = 0
                self.perimeter_defense = 0
                self.block_max = 90
                self.steal_max = 90
                self.perimeter_defense_max = 90 
                self.attr_points = 0
        elif user_archetype.upper() == "POST SCORER" or user_archetype.upper() == "POSTSCORER":
            self.archetype = "Post Scorer"
            self.post_control = 0
            self.post_hook = 0
            self.post_fadeaway = 0
            self.post_control_max = 90
            self.post_hook_max = 90
            self.post_fadeaway_max = 90 
            self.attr_points = 0
        elif user_archetype.upper() == "GLASS CLEANER" or user_archetype.upper() == "GLASSCLEANER":
            self.archetype = "Glass Cleaner"
            self.offensive_rebound = 0
            self.defensive_rebound = 0
            self.box_out = 0
            self.offensive_rebound_max = 90
            self.defensive_rebound_max = 90
            self.box_out_max = 90 
            self.attr_points = 0
        
        
    def pass_accuracy_change(self, change_type, value_change):
        if change_type == "I":
            if (self.pass_accuracy + value_change) > self.pass_accuracy_max:
                print(f"Cannot do this action as it would lead to you going over the max Passing Accuracy level ({self.pass_accuracy_max}).\n")
                sleep(2.0)
            elif (self.pass_accuracy + value_change) < 0:
                print("Cannot do this action as it would lead to Passing Accuracy being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.pass_accuracy += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.pass_accuracy - value_change) > self.pass_accuracy_max:
                print(f"Cannot do this action as it would lead to you going over the max Passing Accuracy level ({self.pass_accuracy_max}).\n")
                sleep(2.0)
            elif (self.pass_accuracy - value_change) < 0:
                print("Cannot do this action as it would lead to Passing Accuracy being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.pass_accuracy -= value_change 
                self.attr_points -= value_change
    
    def ball_handle_change(self, change_type, value_change):
        if change_type == "I":
            if (self.ball_handle + value_change) > self.ball_handle_max:
                print(f"Cannot do this action as it would lead to you going over the max Ball Handle level ({self.ball_handle_max}).\n")
                sleep(2.0)
            elif (self.ball_handle + value_change) < 0:
                print("Cannot do this action as it would lead to Ball Handle being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.ball_handle += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.ball_handle - value_change) > self.ball_handle_max:
                print(f"Cannot do this action as it would lead to you going over the max Ball Handle level ({self.ball_handle_max}).\n")
                sleep(2.0)
            elif (self.ball_handle - value_change) < 0:
                print("Cannot do this action as it would lead to Ball Handle being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.ball_handle -= value_change 
                self.attr_points -= value_change
    
    def speed_with_ball_change(self, change_type, value_change):
        if change_type == "I":
            if (self.speed_with_ball + value_change) > self.speed_with_ball_max:
                print(f"Cannot do this action as it would lead to you going over the max Speed with Ball level ({self.speed_with_ball_max}).\n")
                sleep(2.0)
            elif (self.speed_with_ball + value_change) < 0:
                print("Cannot do this action as it would lead to Speed with Ball being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.speed_with_ball += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.speed_with_ball - value_change) > self.speed_with_ball_max:
                print(f"Cannot do this action as it would lead to you going over the max Speed with Ball level ({self.speed_with_ball_max}).\n")
                sleep(2.0)
            elif (self.speed_with_ball - value_change) < 0:
                print("Cannot do this action as it would lead to Speed with Ball being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.speed_with_ball -= value_change 
                self.attr_points -= value_change
    
    def driving_layup_change(self, change_type, value_change):
        if change_type == "I":
            if (self.driving_layup + value_change) > self.driving_layup_max:
                print(f"Cannot do this action as it would lead to you going over the max Driving Layup level ({self.driving_layup_max}).\n")
                sleep(2.0)
            elif (self.driving_layup + value_change) < 0:
                print("Cannot do this action as it would lead to Driving Layup being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.driving_layup += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.driving_layup - value_change) > self.driving_layup_max:
                print(f"Cannot do this action as it would lead to you going over the max Driving Layup level ({self.driving_layup_max}).\n")
                sleep(2.0)
            elif (self.driving_layup - value_change) < 0:
                print("Cannot do this action as it would lead to Driving Layup being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.driving_layup -= value_change
                self.attr_points -= value_change
    
    def driving_dunk_change(self, change_type, value_change):
        if change_type == "I":
            if (self.driving_dunk + value_change) > self.driving_dunk_max:
                print(f"Cannot do this action as it would lead to you going over the max Driving Dunk level ({self.driving_dunk_max}).\n")
                sleep(2.0)
            elif (self.driving_dunk + value_change) < 0:
                print("Cannot do this action as it would lead to Driving Dunk being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.driving_dunk += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.driving_dunk - value_change) > self.driving_dunk_max:
                print(f"Cannot do this action as it would lead to you going over the max Driving Dunk level ({self.driving_dunk_max}).\n")
                sleep(2.0)
            elif (self.driving_dunk - value_change) < 0:
                print("Cannot do this action as it would lead to Driving Dunk being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.driving_dunk -= value_change
                self.attr_points -= value_change
    
    def standing_dunk_change(self, change_type, value_change):
        if change_type == "I":
            if (self.standing_dunk + value_change) > self.standing_dunk_max:
                print(f"Cannot do this action as it would lead to you going over the max Standing Dunk level ({self.standing_dunk_max}).\n")
                sleep(2.0)
            elif (self.standing_dunk + value_change) < 0:
                print("Cannot do this action as it would lead to Standing Dunk being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.standing_dunk += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.standing_dunk - value_change) > self.standing_dunk_max:
                print(f"Cannot do this action as it would lead to you going over the max Standing Dunk level ({self.standing_dunk_max}).\n")
                sleep(2.0)
            elif (self.standing_dunk - value_change) < 0:
                print("Cannot do this action as it would lead to Standing Dunk being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.standing_dunk -= value_change
                self.attr_points -= value_change
    
    def contested_shot_change(self, change_type, value_change):
        if change_type == "I":
            if (self.contested_shot + value_change) > self.contested_shot_max:
                print(f"Cannot do this action as it would lead to you going over the max Contested Shot level ({self.contested_shot_max}).\n")
                sleep(2.0)
            elif (self.contested_shot + value_change) < 0:
                print("Cannot do this action as it would lead to Contested Shot being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.contested_shot += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.contested_shot - value_change) > self.contested_shot_max:
                print(f"Cannot do this action as it would lead to you going over the max Contested Shot level ({self.contested_shot_max}).\n")
                sleep(2.0)
            elif (self.contested_shot - value_change) < 0:
                print("Cannot do this action as it would lead to Contested Shot being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.contested_shot -= value_change
                self.attr_points -= value_change

    def post_fadeaway_change(self, change_type, value_change):
        if change_type == "I":
            if (self.post_fadeaway + value_change) > self.post_fadeaway_max:
                print(f"Cannot do this action as it would lead to you going over the max Post Fadeaway level ({self.post_fadeaway_max}).\n")
                sleep(2.0)
            elif (self.post_fadeaway + value_change) < 0:
                print("Cannot do this action as it would lead to Post Fadeaway being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.post_fadeaway += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.post_fadeaway - value_change) > self.post_fadeaway_max:
                print(f"Cannot do this action as it would lead to you going over the max Post Fadeaway level ({self.post_fadeaway_max}).\n")
                sleep(2.0)
            elif (self.post_fadeaway - value_change) < 0:
                print("Cannot do this action as it would lead to Post Fadeaway being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.post_fadeaway -= value_change
                self.attr_points -= value_change

    def off_dribble_shot_change(self, change_type, value_change):
        if change_type == "I":
            if (self.off_dribble_shot + value_change) > self.off_dribble_shot_max:
                print(f"Cannot do this action as it would lead to you going over the max Off-Dribble Shot level ({self.off_dribble_shot_max}).\n")
                sleep(2.0)
            elif (self.off_dribble_shot + value_change) < 0:
                print("Cannot do this action as it would lead to Off-Dribble Shot being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.off_dribble_shot += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.off_dribble_shot - value_change) > self.off_dribble_shot_max:
                print(f"Cannot do this action as it would lead to you going over the max Off-Dribble Shot level ({self.off_dribble_shot_max}).\n")
                sleep(2.0)
            elif (self.off_dribble_shot - value_change) < 0:
                print("Cannot do this action as it would lead to Off-Dribble Shot being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.off_dribble_shot -= value_change
                self.attr_points -= value_change
    
    def mid_range_change(self, change_type, value_change):
        if change_type == "I":
            if (self.mid_range + value_change) > self.mid_range_max:
                print(f"Cannot do this action as it would lead to you going over the max Mid-Range level ({self.mid_range_max}).\n")
                sleep(2.0)
            elif (self.mid_range + value_change) < 0:
                print("Cannot do this action as it would lead to Mid-Range being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.mid_range += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.mid_range - value_change) > self.mid_range_max:
                print(f"Cannot do this action as it would lead to you going over the max Mid-Range level ({self.mid_range_max}).\n")
                sleep(2.0)
            elif (self.mid_range - value_change) < 0:
                print("Cannot do this action as it would lead to Mid-Range being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.mid_range -= value_change
                self.attr_points -= value_change
        
    def three_point_change(self, change_type, value_change):
        if change_type == "I":
            if (self.three_point + value_change) > self.three_point_max:
                print(f"Cannot do this action as it would lead to you going over the max Three Pointer level ({self.three_point_max}).\n")
                sleep(2.0)
            elif (self.three_point + value_change) < 0:
                print("Cannot do this action as it would lead to Three Pointer being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.three_point += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.three_point - value_change) > self.three_point_max:
                print(f"Cannot do this action as it would lead to you going over the max Three Pointer level ({self.three_point_max}).\n")
                sleep(2.0)
            elif (self.three_point - value_change) < 0:
                print("Cannot do this action as it would lead to Three Pointer being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.three_point -= value_change
                self.attr_points -= value_change

    def free_throw_change(self, change_type, value_change):
        if change_type == "I":
            if (self.free_throw + value_change) > self.free_throw_max:
                print(f"Cannot do this action as it would lead to you going over the max Free Throw level ({self.free_throw_max}).\n")
                sleep(2.0)
            elif (self.free_throw + value_change) < 0:
                print("Cannot do this action as it would lead to Free Throw level being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.free_throw += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.free_throw - value_change) > self.free_throw_max:
                print(f"Cannot do this action as it would lead to you going over the max Free Throw level ({self.free_throw_max}).\n")
                sleep(2.0)
            elif (self.free_throw - value_change) < 0:
                print("Cannot do this action as it would lead to Free Throw level being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.free_throw -= value_change
                self.attr_points -= value_change

    def block_change(self, change_type, value_change):
        if change_type == "I":
            if (self.block + value_change) > self.block_max:
                print(f"Cannot do this action as it would lead to you going over the max Block level ({self.block_max}).\n")
                sleep(2.0)
            elif (self.block + value_change) < 0:
                print("Cannot do this action as it would lead to Block being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.block += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.block - value_change) > self.block_max:
                print(f"Cannot do this action as it would lead to you going over the max Block level ({self.block_max}).\n")
                sleep(2.0)
            elif (self.block - value_change) < 0:
                print("Cannot do this action as it would lead to Block being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.block -= value_change
                self.attr_points -= value_change
    
    def steal_change(self, change_type, value_change):
        if change_type == "I":
            if (self.steal + value_change) > self.steal_max:
                print(f"Cannot do this action as it would lead to you going over the max Steal level ({self.steal_max}).\n")
                sleep(2.0)
            elif (self.steal + value_change) < 0:
                print("Cannot do this action as it would lead to Steal being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.steal += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.steal - value_change) > self.steal_max:
                print(f"Cannot do this action as it would lead to you going over the max Steal level ({self.steal_max}).\n")
                sleep(2.0)
            elif (self.steal - value_change) < 0:
                print("Cannot do this action as it would lead to Steal being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.steal -= value_change
                self.attr_points -= value_change
    
    def perimeter_defense_change(self, change_type, value_change):
        if change_type == "I":
            if (self.perimeter_defense + value_change) > self.perimeter_defense_max:
                print(f"Cannot do this action as it would lead to you going over the max Perimeter Defense level ({self.perimeter_defense_max}).\n")
                sleep(2.0)
            elif (self.perimeter_defense + value_change) < 0:
                print("Cannot do this action as it would lead to Perimeter Defense being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.perimeter_defense += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.perimeter_defense - value_change) > self.perimeter_defense_max:
                print(f"Cannot do this action as it would lead to you going over the max Perimeter Defense level ({self.perimeter_defense_max}).\n")
                sleep(2.0)
            elif (self.perimeter_defense - value_change) < 0:
                print("Cannot do this action as it would lead to Perimeter Defense being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.perimeter_defense -= value_change
                self.attr_points -= value_change

    def interior_defense_change(self, change_type, value_change):
        if change_type == "I":
            if (self.interior_defense + value_change) > self.interior_defense_max:
                print(f"Cannot do this action as it would lead to you going over the max Interior Defense level ({self.interior_defense_max}).\n")
                sleep(2.0)
            elif (self.interior_defense + value_change) < 0:
                print("Cannot do this action as it would lead to Interior Defense being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.interior_defense += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.interior_defense - value_change) > self.interior_defense_max:
                print(f"Cannot do this action as it would lead to you going over the max Interior Defense level ({self.interior_defense_max}).\n")
                sleep(2.0)
            elif (self.interior_defense - value_change) < 0:
                print("Cannot do this action as it would lead to Interior Defense being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.interior_defense -= value_change
                self.attr_points -= value_change
    
    def post_control_change(self, change_type, value_change):
        if change_type == "I":
            if (self.post_control + value_change) > self.post_control_max:
                print(f"Cannot do this action as it would lead to you going over the max Post Control level ({self.post_control_max}).\n")
                sleep(2.0)
            elif (self.post_control + value_change) < 0:
                print("Cannot do this action as it would lead to Post Control being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.post_control += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.post_control - value_change) > self.post_control_max:
                print(f"Cannot do this action as it would lead to you going over the max Post Control level ({self.post_control_max}).\n")
                sleep(2.0)
            elif (self.post_control - value_change) < 0:
                print("Cannot do this action as it would lead to Post Control being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.post_control -= value_change
                self.attr_points -= value_change

    def post_hook_change(self, change_type, value_change):
        if change_type == "I":
            if (self.post_hook + value_change) > self.post_hook_max:
                print(f"Cannot do this action as it would lead to you going over the max Post Hook level ({self.post_hook_max}).\n")
                sleep(2.0)
            elif (self.post_hook + value_change) < 0:
                print("Cannot do this action as it would lead to Post Hook being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.post_hook += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.post_hook - value_change) > self.post_hook_max:
                print(f"Cannot do this action as it would lead to you going over the max Post Hook level ({self.post_hook_max}).\n")
                sleep(2.0)
            elif (self.post_hook - value_change) < 0:
                print("Cannot do this action as it would lead to Post Hook being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.post_hook -= value_change
                self.attr_points -= value_change
    
    def box_out_change(self, change_type, value_change):
        if change_type == "I":
            if (self.box_out + value_change) > self.box_out_max:
                print(f"Cannot do this action as it would lead to you going over the max Box Out level ({self.box_out_max}).\n")
                sleep(2.0)
            elif (self.box_out + value_change) < 0:
                print("Cannot do this action as it would lead to Box Out being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.box_out += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.box_out - value_change) > self.box_out_max:
                print(f"Cannot do this action as it would lead to you going over the max Box Out level ({self.box_out_max}).\n")
                sleep(2.0)
            elif (self.box_out - value_change) < 0:
                print("Cannot do this action as it would lead to Box Out being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.box_out -= value_change
                self.attr_points -= value_change
    
    def offensive_rebound_change(self, change_type, value_change):
        if change_type == "I":
            if (self.offensive_rebound + value_change) > self.offensive_rebound_max:
                print(f"Cannot do this action as it would lead to you going over the max Offensive Rebound level ({self.offensive_rebound_max}).\n")
                sleep(2.0)
            elif (self.offensive_rebound + value_change) < 0:
                print("Cannot do this action as it would lead to Offensive Rebound being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.offensive_rebound += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.offensive_rebound - value_change) > self.offensive_rebound_max:
                print(f"Cannot do this action as it would lead to you going over the max Offensive Rebound level ({self.offensive_rebound_max}).\n")
                sleep(2.0)
            elif (self.offensive_rebound - value_change) < 0:
                print("Cannot do this action as it would lead to Offensive Rebound being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.offensive_rebound -= value_change
                self.attr_points -= value_change
    
    def defensive_rebound_change(self, change_type, value_change):
        if change_type == "I":
            if (self.defensive_rebound + value_change) > self.defensive_rebound_max:
                print(f"Cannot do this action as it would lead to you going over the max Defensive Rebound level ({self.defensive_rebound_max}).\n")
                sleep(2.0)
            elif (self.defensive_rebound + value_change) < 0:
                print("Cannot do this action as it would lead to Defensive Rebound being negative.\n")
                sleep(2.0)
            elif (self.attr_points + value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points + value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.defensive_rebound += value_change
                self.attr_points += value_change
        elif change_type == "D":
            if (self.defensive_rebound - value_change) > self.defensive_rebound_max:
                print(f"Cannot do this action as it would lead to you going over the max Defensive Rebound level ({self.defensive_rebound_max}).\n")
                sleep(2.0)
            elif (self.defensive_rebound - value_change) < 0:
                print("Cannot do this action as it would lead to Defensive Rebound being negative.\n")
                sleep(2.0)
            elif (self.attr_points - value_change) > 255:
                print(f"Cannot do this action. Not enough Attribute Points to do so ({self.attr_points} Attribute Points left).\n")
                sleep(2.0)
            elif (self.attr_points - value_change) < 0:
                print("Cannot do this action. Leads to Attribute Points being negative.\n")
                sleep(2.0)
            else:
                self.defensive_rebound -= value_change
                self.attr_points -= value_change

    def __str__(self):
        if self.archetype == "Playmaker":
            return f"Archetype: {self.archetype}\nPassing Accuracy: {self.pass_accuracy}\nBall Handle: {self.ball_handle}\nSpeed with Ball: {self.speed_with_ball}\n" 
        elif self.archetype == "Slasher":
            return f"Archetype: {self.archetype}\nDriving Layup: {self.driving_layup}\nDriving Dunk: {self.driving_dunk}\nStanding Dunk: {self.standing_dunk}\n"
        elif self.archetype == "Shot Creator":
            return f"Archetype: {self.archetype}\nPost Fadeaway: {self.post_fadeaway}\nContested Shot: {self.contested_shot}\nOff-Dribble Shot: {self.off_dribble_shot}\n"
        elif self.archetype == "Sharpshooter":
            return f"Archetype: {self.archetype}\nFree Throw: {self.free_throw}\nMid-Range: {self.mid_range}\nThree Pointer: {self.three_point}\n"
        elif self.archetype == "Lockdown":
            if my_player.position == "Center" or my_player.position == "Power Forward" or my_player.position == "Small Forward": 
                return f"Archetype: {self.archetype}\nBlock: {self.block}\nSteal: {self.steal}\nInterior Defense: {self.interior_defense}\n"
            else:
                return f"Archetype: {self.archetype}\nBlock: {self.block}\nSteal: {self.steal}\nPerimeter Defense: {self.perimeter_defense}\n"
        elif self.archetype == "Post Scorer":
            return f"Archetype: {self.archetype}\nPost Control: {self.post_control}\nPost Hook: {self.post_hook}\nPost Fadeaway: {self.post_fadeaway}\n"
        elif self.archetype == "Glass Cleaner":
            return f"Archetype: {self.archetype}\nBox Out: {self.box_out}\nOffensive Rebound: {self.offensive_rebound}\nDefensive Rebound: {self.defensive_rebound}\n"
        
    def print_maxes(self):
        if self.archetype == "Playmaker":
            print(f"Archetype: {self.archetype}\nPassing Accuracy: {self.pass_accuracy_max}\nBall Handle: {self.ball_handle_max}\nSpeed with Ball: {self.speed_with_ball_max}\n") 
        elif self.archetype == "Slasher":
            print(f"Archetype: {self.archetype}\nDriving Layup: {self.driving_layup_max}\nDriving Dunk: {self.driving_dunk_max}\nStanding Dunk: {self.standing_dunk_max}\n")
        elif self.archetype == "Shot Creator":
            print(f"Archetype: {self.archetype}\nPost Fadeaway: {self.post_fadeaway_max}\nContested Shot: {self.contested_shot_max}\n Off-Dribble Shot: {self.off_dribble_shot_max}\n")
        elif self.archetype == "Sharpshooter":
            print(f"Archetype: {self.archetype}\nFree Throw: {self.free_throw_max}\nMid-Range: {self.mid_range_max}\nThree Pointer: {self.three_point_max}\n")
        elif self.archetype == "Lockdown":
            if my_player.position == "Center" or my_player.position == "Power Forward" or my_player.position == "Small Forward": 
                print(f"Archetype: {self.archetype}\nBlock: {self.block_max}\nSteal: {self.steal_max}\nInterior Defense: {self.interior_defense_max}\n")
            else:
                print(f"Archetype: {self.archetype}\nBlock: {self.block_max}\nSteal: {self.steal_max}\nPerimeter Defense: {self.perimeter_defense_max}\n")
        elif self.archetype == "Post Scorer":
            print(f"Archetype: {self.archetype}\nPost Control: {self.post_control_max}\nPost Hook: {self.post_hook_max}\nPost Fadeaway: {self.post_fadeaway_max}\n")
        elif self.archetype == "Glass Cleaner":
            print(f"Archetype: {self.archetype}\nBox Out: {self.box_out_max}\nOffensive Rebound: {self.offensive_rebound_max}\nDefensive Rebound: {self.defensive_rebound_max}\n")
    
    def stat_status(self, attribute):
        if attribute == "BALL HANDLE":
            return f"Ball Handle Current Level: {self.ball_handle}, Ball Handle Max Level: {self.ball_handle_max}"
        elif attribute == "SPEED WITH BALL":
            return f"Speed with Ball Current Level: {self.speed_with_ball}, Speed with Ball Max Level: {self.speed_with_ball_max}"
        elif attribute == "PASSING ACCURACY":
            return f"Passing Accuracy Current Level: {self.pass_accuracy}, Passing Accuracy Max Level: {self.pass_accuracy_max}"
        elif attribute == "THREE POINTER":
            return f"Three Pointer Current Level: {self.three_point}, Three Pointer Max Level: {self.three_point_max}"
        elif attribute == "MID-RANGE":
            return f"Mid-Range Current Level: {self.mid_range}, Mid-Range Max Level: {self.pass_accuracy_max}"
        elif attribute == "FREE THROW":
            return f"Free Throw Current Level: {self.free_throw}, Free Throw Max Level: {self.free_throw_max}"
        elif attribute == "DRIVING DUNK":
            return f"Driving Dunk Current Level: {self.driving_dunk}, Driving Dunk Max Level: {self.driving_dunk_max}"
        elif attribute == "DRIVING LAYUP":
            return f"Driving Layup Current Level: {self.driving_layup}, Driving Layup Max Level: {self.driving_layup_max}"
        elif attribute == "STANDING DUNK":
            return f"Standing Dunk Current Level: {self.standing_dunk}, Standing Dunk Max Level: {self.standing_dunk_max}"
        elif attribute == "OFF-DRIBBLE SHOT":
            return f"Off-Dribble Shot Current Level: {self.off_dribble_shot}, Off-Dribble Shot Max Level: {self.off_dribble_shot_max}"
        elif attribute == "CONTESTED SHOT":
            return f"Contested Shot Current Level: {self.contested_shot}, Contested Shot Max Level: {self.contested_shot_max}"
        elif attribute == "POST FADEAWAY":
            return f"Post Fadeaway Current Level: {self.post_fadeaway}, Post Fadeaway Max Level: {self.post_control_max}"
        elif attribute == "PERIMETER DEFENSE":
            return f"Perimeter Defense Current Level: {self.perimeter_defense}, Perimeter Defense Max Level: {self.perimeter_defense_max}"
        elif attribute == "INTERIOR DEFENSE":
            return f"Interior Defense Current Level: {self.interior_defense}, Interior Defense Max Level: {self.interior_defense_max}"
        elif attribute == "STEAL":
            return f"Steal Current Level: {self.steal}, Steal Max Level: {self.steal_max}"
        elif attribute == "BLOCK":
            return f"Block Current Level: {self.block}, Block Max Level: {self.block_max}"
        elif attribute == "POST CONTROL":
            return f"Post Control Current Level: {self.post_control}, Post Control Max Level: {self.post_control_max}"
        elif attribute == "POST HOOK":
            return f"Post Hook Current Level: {self.post_hook}, Post Hook Max Level: {self.post_hook_max}"
        elif attribute == "BOX OUT":
            return f"Box Out Current Level: {self.box_out}, Box Out Max Level: {self.box_out_max}"
        elif attribute == "OFFENSIVE REBOUND":
            return f"Offensive Rebound Current Level: {self.offensive_rebound}, Offensive Rebound Max Level: {self.offensive_rebound_max}"
        elif attribute == "DEFENSIVE REBOUND":
            return f"Defensive Rebound Current Level: {self.defensive_rebound}, Defensive Rebound Max Level: {self.defensive_rebound_max}"

nba_teams = ["ATLANTA HAWKS", "BOSTON CELTICS", "BROOKLYN NETS", "CHARLOTTE HORNETS", "CHICAGO BULLS", 
"CLEVELAND CAVALIERS", "DALLAS MAVERICKS", "DENVER NUGGETS", "DETROIT PISTONS", "GOLDEN STATE WARRIORS", 
"HOUSTON ROCKETS", "INDIANA PACERS", "LA CLIPPERS", "LA LAKERS", "MEMPHIS GRIZZLIES", "MIAMI HEAT", 
"MILWAUKEE BUCKS", "MINNESOTA TIMBERWOLVES", "NEW ORLEANS PELICANS", "NEW YORK KNICKS", "OKLAHOMA CITY THUNDER", 
"ORLANDO MAGIC", "PHILADELPHIA SIXERS", "PHOENIX SUNS", "PORTLAND TRAIL BLAZERS", "SACRAMENTO KINGS", "SAN ANTONIO SPURS",
"TORONTO RAPTORS", "UTAH JAZZ", "WASHINGTON WIZARDS"]

team_retired_jerseys = {"Atlanta Hawks"   : [9, 21, 23, 44, 55, 59],
                        "Boston Celtics"   : [00, 1, 2, 3, 5, 6, 10, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35],
                        "Brooklyn Nets" : [4, 25, 32, 23, 3, 52],
                        "Charlotte Hornets" : [13],
                        "Chicago Bulls"  : [4, 10, 23, 33],
                        "Cleveland Cavaliers" : [7, 11, 22, 25, 34, 42, 43],
                        "Dallas Mavericks" : [6, 12, 15, 22, 41],
                        "Denver Nuggets": [2, 12, 33, 40, 44, 55, 432],
                        "Detroit Pistons": [1, 2, 3, 4, 10, 11, 15, 16, 21, 32, 40],
                        "Golden State Warriors": [13, 14, 16, 17, 24, 42],
                        "Houston Rockets": [11, 22, 23, 24, 34, 45],
                        "Indiana Pacers": [30, 31, 34, 35, 529],
                        "La Clippers": [''],
                        "La Lakers": [24, 32, 8, 13, 22, 25, 33, 34, 42, 44, 52],
                        "Memphis Grizzlies": [9, 50],
                        "Miami Heat": [1, 3, 10, 13, 23, 32, 33],
                        "Milwaukee Bucks": [1, 2, 4, 8, 10, 14, 16, 32, 33],
                        "Minnesota Timberwolves": [2],
                        "New Orleans Pelicans": [7],
                        "New York Knicks": [10, 12, 15, 15, 19, 22, 24, 33, 613],
                        "Oklahoma City Thunder": [1, 4, 10, 19, 24, 32, 43],
                        "Orlando Magic": [6],
                        "Philadelphia Sixers": [2, 4, 3, 34, 10, 13, 6, 24, 32, 15],
                        "Phoenix Suns": [5, 6, 7, 9, 13, 24, 33, 34, 42, 44],
                        "Portland Trail Blazers": [1, 13, 14, 15, 20, 22, 30, 30, 32, 36, 45, 77],
                        "Sacramento Kings": [1, 2, 4, 6, 11, 12, 14, 16, 21, 27, 44],
                        "San Antonio Spurs": [00, 6, 9, 12, 13, 20, 21, 32, 44, 50],
                        "Toronto Raptors": [''],
                        "Utah Jazz": [1, 4, 7, 9, 12, 14, 32, 35, 53, 1223],
                        "Washington Wizards": [10, 11, 25, 41, 45]
                        }

colleges = ["DUKE", "KANSAS", 
"FLORIDA", "UCLA", "VILLANOVA", "OKLAHOMA", "MICHIGAN STATE", 
"GONZAGA", "SYRACUSE", "UCONN", "TEXAS TECH", "WEST VIRGINIA"]

"""
^^^^
- List of all NBA teams
- List of all NBA teams and their retired jerseys.
- List of all D1 college options for users to pick from. 
"""

def ready():
    """
    - Helper function 
    - Asks the user if they are ready to proceed with the MyPlayer creation process 
    - Usually used after instructions are given
    """
    while True:
        ready = input("Are you ready? [Yes or No]: ").upper().strip()
        sleep(2.0)
        if ready == "YES":
            print("\nAlright\n")
            sleep(2.0)
            break
        elif ready == "NO":
            print("\nTake your time.\n")
            sleep(2.0)
            continue
        else:
            print("\nPlease enter either \"Yes\" or \"No\".\n")
            continue

def uppercase_start(string):
    """
    - Helper function 
    - Takes a string 
    - Returns string with every word separated by a space starting with an uppercase letter
    """
    s_return = "" 
    word_list = (str(string)).split(" ") 
    cnt = 0 
    for word in word_list:  
        curr_word = word[0] 
        if curr_word.isalpha() == True:   
            curr_word = word[0].upper()  
            for i in range(1,len(word)):
                curr_word += word[i].lower() 
        else: 
            for i in range(1,len(word)):
                curr_word += word[i].lower()
        cnt += 1 
        if cnt == len(word_list):  
            s_return += curr_word 
        else:  
            s_return += curr_word + " " 
    
    return s_return 

def leave_or_stay(attribute_points, adjust_Type = "Base"):
    """
    - Helper function 
    - Used in two functions (adjust_base_stats(), adjust_arch_stats())
    - We know which function it is called under based on arguments passed
    - Called when user still types "DONE" in one of the two functions listed above
    - If user still has more attribute points left to use, function asks if user still wants to leave
    - We know how much attribute points are left and the max attribute points based on arguments passed
    """
    leave = True
    max_attribute_points = 230 
    if adjust_Type == "Archetype":
        max_attribute_points = 255
    if attribute_points < max_attribute_points:
        while True:
            exit_choice = input(f"\nAre you sure you want to exit? You still have {max_attribute_points - attribute_points}/{max_attribute_points} Attribute Points left. [Yes or No]: ").strip() 
            sleep(2.0)
            if exit_choice.upper() == "YES":
                break
            elif exit_choice.upper() == "NO":
                leave = False
                break
            else:
                print("\nPlease enter either \"Yes\" or \"No\".")
                continue
                
    return leave
    
def intro():
    """
    - Introduces user to MyPlayer builder
    - Gets user name
    """
    global user_name
    print("Welcome to the NBA MyPlayer builder!\n")
    sleep(2.0)
    print("In this tool, you will have the opportunity to create and customize your very own NBA player.\n")
    sleep(2.0)
    print("You will be able to choose your player's background, attributes, NBA team, and skill set to create a unique character that represents your style of play.\n") 
    sleep(2.0)
    print("Whether you prefer to be a dominant center, a crafty point guard, or anything in between, you'll have the freedom to build your MyPlayer exactly how you want.\n") 
    sleep(2.0)
    print("So let's get started on creating your dream NBA player!\n")
    sleep(2.0)
    print("Before we get started, let's get your name.\n")
    sleep(2.0)
    while True:
        first_name = input("Enter your first name here: ").strip()
        sleep(2.0)
        if first_name.isalpha() == False:
            print("\nYour name cannot include any numbers or special characters.\n") 
            continue
        if len(first_name) > 20:
            print("\nYour first name cannot be longer than 20 letters.\n") 
            continue
        else:
            break
    while True:
        last_name = input("\nEnter your last name here: ").strip()
        sleep(2.0)
        if last_name.isalpha() == False:
            print("\nYour name cannot include any numbers or special characters.") 
            continue
        if len(last_name) > 20:
            print("\nYour last name cannot be longer than 20 letters.") 
            continue
        else:
            break
    user_name = uppercase_start(first_name.strip()) + " " + uppercase_start(last_name.strip())
    print(f"\nWelcome {user_name}, the league doesn't know what hit them.\n")

def position():
    """
    - Asks user which position they would like to play
    - Users choice has an affect on attributes of Player_base object created in adjust_base_stats() function
    """
    global user_position
    while True:
        user_position = input("Enter what position you would like to be [Point Guard, Shooting Guard, Small Forward, Power Forward, Center]: ").strip()
        sleep(2.0)
        positions = ["PG", "POINT GUARD", "SG", "SHOOTING GUARD", "SF", "SMALL FORWARD", "PF", "POWER FORWARD", "C", "CENTER"]
        if user_position.upper() not in positions:
            print("\nPlease enter one of the listed positions.\n") 
            continue
        else:
            break   

def adjust_base_stats():
    """
    - Creates Player_base object for user
    - User is allowed to adjust his base stats 
    - 4 base stats in total (Speed, Strength, Acceleration, Vertical)
    - User base stats all start as 0
    - Given 230 attribute points to spread along the 4 base stats
    - Each position has a max level for each base stat
    """
    
    global my_player
    my_player = Player_base()
    print("\nWelcome to the first step of the MyPlayer builder. Here, you will be adjusting your base stats.\n")
    sleep(2.0)
    print("In this builder, we have prioritized 4 base stats. Speed, Strength, Acceleration, and Vertical.\n")
    sleep(2.0)
    print("Currently, every one of your base stats are set to zero.\n")
    sleep(2.0)
    print(my_player)
    sleep(2.0)
    print("You will get 230 points to spend across your stats. We call these Attribute Points.\n")
    sleep(2.0)
    print("You cannot go over the assigned 230 attribute points or make it negative.\n")
    sleep(2.0)
    print("In addition, every position has a max level on every stat.\n")
    sleep(2.0)
    print(f"In your case, as a {my_player.position}, these are the max levels for every base stat.\n")
    sleep(2.0)
    my_player.print_maxes() 
    sleep(2.0)
    print("Throughout the process, if you are done with adjusting your base stats, simply type \"Done\" for any of the prompts.\n")
    sleep(2.0)
    ready()



    while True:
        try: 
            attribute_change = input("Attribute to change? [Speed, Strength, Acceleration, Vertical]: ").strip()
            if attribute_change.upper() == "DONE":
                if leave_or_stay(my_player.attr_points) == True:
                    break
                else:
                    continue
            if attribute_change.isnumeric() ==  True:
                raise ValueError
            if attribute_change.upper() != "SPEED" and attribute_change.upper() != "STRENGTH" and attribute_change.upper() != "ACCELERATION" and attribute_change.upper() != "VERTICAL" and attribute_change.upper() != "DONE":
                raise TypeError
        except ValueError:
            print("\nSorry, we couldn't process that request. Please enter one of these 4 attributes [Speed, Strength, Acceleration, Vertical] or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except TypeError:
            print("\nSorry, we couldn't process that request. Please enter one of these 4 attributes [Speed, Strength, Acceleration, Vertical] or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except:
            print("\nSorry, we couldn't process that request. Please enter one of these 4 attributes [Speed, Strength, Acceleration, Vertical] or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        
        try:
            type_change = input("\nEnter \"I\" if you want to increase a stat, or \"D\" if you want to decrease a stat: ").strip()
            if type_change.upper() == "DONE":
                if leave_or_stay(my_player.attr_points) == True:
                    break
                else:
                    continue 
            if type_change.isnumeric() ==  True:
                raise ValueError
            if type_change.upper() != "I" and type_change.upper() != "D" and type_change.upper() != "DONE":
                raise TypeError
        except ValueError:
            print("\nSorry, we couldn't process that request. Please enter either \"I\" to increase the stat or \"D\" to decrease the stat or just \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except TypeError:
            print("\nSorry, we couldn't process that request. Please enter either \"I\" to increase the stat or \"D\" to decrease the stat or just \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except:
            print("\nSorry, we couldn't process that request. Please enter either \"I\" to increase the stat or \"D\" to decrease the stat or just \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue

        try:
            value_change = input(f"\nBy how much would you like to make this change? [{my_player.stat_status(attribute_change.upper())}]: ").strip()
            if value_change.upper() == "DONE":
                if leave_or_stay(my_player.attr_points) == True:
                    break
                else:
                    continue 
            if value_change.upper() != "DONE" and value_change.isalpha() ==  True:
                raise ValueError
        except ValueError:
            print("\nSorry, we couldn't process that request. Please enter either a number to increase of decrease the stat or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except:
            print("\nSorry, we couldn't process that request. Please enter either a number to increase of decrease the stat or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        print("")
    
        if attribute_change.upper() == "SPEED":
            my_player.speed_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "STRENGTH":
            my_player.strength_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "ACCELERATION":
            my_player.acceleration_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "VERTICAL":
            my_player.vertical_change(type_change.upper(),int(value_change))
        
        print("Here are your current stats: \n")
        sleep(2.0)
        print(my_player)
        sleep(2.0)
        print(f"Current Attribute Points Used: {my_player.attr_points}.\n")
        print(f"Current Attribute Points left: {230 - my_player.attr_points}.\n")

def height():
    """
    - Asks user what height they would like to be
    - Every height has 5 heights allowed for them
    - Height chosen will have varying effects on user base stats within Player_base object 
    """
    global my_player
    global user_height
    pg_height = ("6'0", "6'1", "6'2", "6'3", "6,4")
    sg_height = ("6'3", "6'4", "6'5", "6'6", "6'7")
    sf_height = ("6'6", "6'7", "6'8", "6'9", "6'10")
    pf_height = ("6'8", "6'9", "6'10", "6'11", "7'0")
    c_height = ("6'10", "6'11", "7'0", "7'1", "7'2")
    print("\nFor the next step of the MyPlayer builder, you will be choosing your height.\n")
    sleep(2.0)
    print("Every position has a set range of heights they are allowed to choose from.\n")
    sleep(2.0)
    print("Here are these ranges per position: \n")
    sleep(2.0)
    print(f'Point Guard: {pg_height}')
    print(f'Shooting Guard: {sg_height}')
    print(f'Small Forward: {sf_height}')
    print(f'Power Forward: {pf_height}')
    print(f'Center: {c_height}\n')
    sleep(2.0)
    print("If you do not pick one the heights in your specified range, you will be prompted to enter it again.\n")
    sleep(2.0)
    print("In addition, based on the height you choose, different changes will be made to your base stats.\n")
    sleep(2.0)
    print("For example, if you pick a shorter height, you may see an increase in your speed.\n")
    sleep(2.0)
    ready()
    height_table = ()
    if my_player.position == "Point Guard":
        height_table = pg_height
    elif my_player.position == "Shooting Guard":
        height_table = sg_height
    elif my_player.position == "Small Forward":
        height_table = sf_height
    elif my_player.position == "Power Forward":
        height_table = pf_height
    else:
        height_table = c_height
    print(f'Since you are a {my_player.position}, here are your height options: {height_table}.\n')
    while True:
        user_height = input(f"Enter height here {height_table}: ").strip()
        sleep(2.0)
        if user_height not in height_table:
            print("\nPlease enter one of the listed heights.\n")
            continue
        
        if user_height == height_table[0]:
            print(f"\nSpeed Increase: {my_player.speed} -> {my_player.speed + 3}")
            print(f"Strength Decrease: {my_player.strength} -> {my_player.strength - 2}")
            print(f"Acceleration Increase: {my_player.acceleration} -> {my_player.acceleration + 2}")
            print(f"Vertical Increase: {my_player.vertical} -> {my_player.vertical - 2}")
        elif user_height == height_table[1]:
            print(f"\nSpeed Increase: {my_player.speed} -> {my_player.speed + 2}")
            print(f"Strength: {my_player.strength} -> {my_player.strength}")
            print(f"Acceleration Increase: {my_player.acceleration} -> {my_player.acceleration + 2}")
            print(f"Vertical: {my_player.vertical} -> {my_player.vertical}")
        elif user_height == height_table[2]:
            print(f"\nSpeed Increase: {my_player.speed} -> {my_player.speed + 1}")
            print(f"Strength Increase: {my_player.strength} -> {my_player.strength + 1}")
            print(f"Acceleration: {my_player.acceleration} -> {my_player.acceleration}")
            print(f"Vertical Increase: {my_player.vertical} -> {my_player.vertical + 1}")
        elif user_height == height_table[3]:
            print(f"\nSpeed Decrease: {my_player.speed} -> {my_player.speed -1}")
            print(f"Strength Increase: {my_player.strength} -> {my_player.strength + 2}")
            print(f"Acceleration Decrease: {my_player.acceleration} -> {my_player.acceleration - 1}")
            print(f"Vertical Increase: {my_player.vertical} -> {my_player.vertical + 2}")
        elif user_height == height_table[4]:
            print(f"\nSpeed Decrease: {my_player.speed} -> {my_player.speed -2}")
            print(f"Strength Increase: {my_player.strength} -> {my_player.strength + 3}")
            print(f"Acceleration Decrease: {my_player.acceleration} -> {my_player.acceleration - 2}")
            print(f"Vertical Increase: {my_player.vertical} -> {my_player.vertical + 3}")
        
        leave_or_stay = False 
        while True:
            confirmation = input("\nAre you ok with these changes to your stats? [Yes or NO]: ").strip()
            if confirmation.upper() == "YES":
                print("\nALRIGHT!\n")
                if user_height == height_table[0]:
                        my_player.speed += 3
                        my_player.strength -= 2
                        my_player.acceleration += 2
                        my_player.vertical -= 2
                elif user_height == height_table[1]:
                        my_player.speed += 2
                        my_player.acceleration += 2
                elif user_height == height_table[2]:
                        my_player.speed += 1
                        my_player.strength += 1
                        my_player.vertical += 1
                elif user_height == height_table[3]:
                        my_player.speed -= 1
                        my_player.strength += 2
                        my_player.acceleration -= 1
                        my_player.vertical += 2
                elif user_height == height_table[4]:
                        my_player.speed -= 2
                        my_player.strength += 3
                        my_player.acceleration -= 2
                        my_player.vertical += 3
                print(my_player)
                leave_or_stay = True 
                break
            elif confirmation.upper() == "NO":
                print("\nKeep Browsing!\n")
                break
            else:
                print("Yes or NO!\n")
                continue
        
        if leave_or_stay == False:
            continue 
        else:
            break 

def college():
    """
    - User decides which D1 college they attended 
    """
    global user_college
    print("Now it's time to pick what college you are from.\n")
    sleep(2.0)
    print("We will give you the option of 12 D1 schools.\n")
    sleep(2.0)
    print("Here are your options: \n")
    sleep(2.0)
    for x in colleges:
        print(uppercase_start(x))
    sleep(2.0)
    while True: 
        college_choice = input("\nNow make your choice [ENTER THE COLLEGE NAME AS IT IS LISTED ABOVE]: ").strip() 
        sleep(2.0)
        if college_choice.upper() not in colleges:
            print("\nPlease enter the college name as it is listed above.")
            continue
        else:
            user_college = uppercase_start(college_choice.upper())
            print(f"\nCongratulations, you are now a {user_college} alumni.\n")
            break 

def jersey_number():
    """
    - User decides which jersey number they would like to wear
    - Users are not allowed to pick retired jersey numbers 
    - Users must adhere to NBA standard rules regarding jersey numbers 
    """
    global user_team 
    global user_jersey_number
    user_team_retired_jerseys = team_retired_jerseys[user_team]
    print("Now it's time to pick your jersey number!\n")
    sleep(2.0)
    print("Make sure to pick a jersey number that isn't already retired by your respective team.\n")
    sleep(2.0)
    print(f"For a quick reminder, your team is the {user_team} and they have {user_team_retired_jerseys} retired.\n")
    sleep(2.0)
    print("Also remember that the number you choose must be two digits, nothing more.\n")
    sleep(2.0)
    print("Also, the nba has retired #6 in respects to the late great Bill Russel, so that number is also off limits.\n")
    sleep(2.0)
    while True: 
        user_js_num_pick = input("Enter your desired jersey number: ").strip()
        sleep(2.0)
        if user_js_num_pick.isnumeric() == False:
            print("\nYour jersey number cannot include any letters or special characters.\n")
            continue
        if len(user_js_num_pick) > 2:
            print("\nSorry, in the nba, you are only allowed to have a two digit number on the back of your jersey.\n")
            continue 
        if int(user_js_num_pick) == 6:
            print("\nSorry, the NBA has retired #6 in respects to the late great Bill Russel.\n")
            continue 
        if int(user_js_num_pick) in user_team_retired_jerseys:
            print(f"\nSorry, the {user_team} have retired #{user_js_num_pick}.\n")
        else:
            user_jersey_number = int(user_js_num_pick)
            print(f"\nCongratulations, you are #{user_jersey_number} on the {user_team}.\n")
            break  

def team_randomm_choice():
    """
    - Called within team() function based on user input
    - Gives user two randoms to choose from
    - If user doesn't like either teams, they are allowed for one final random that they must stay with
    """
    global user_team
    print("\nAlright, let's give a more in-depth explanation of how this works.\n")
    sleep(2.0)
    print("You will be given two random NBA teams and will get a choice between the two.\n")
    sleep(2.0)
    print("If you decide that you don't like either of the teams, you can go sudden death.\n")
    sleep(2.0)
    print("Sudden death means you get one more random, but you are forced to stick with that team.\n")
    sleep(2.0)
    ready()
    random_1 = uppercase_start(random.choice(nba_teams))
    print(f"Option one is the {random_1}.\n")
    sleep(2.0)
    while True: 
        random_2 = uppercase_start(random.choice(nba_teams))
        if random_2 == random_1:
            continue
        else: 
            print(f"Option two is the {random_2}.\n")
            sleep(2.0)
            break 
    while True:
        random_pick_decision = input("Now that you have seen the two options, it is time to decide. [Type \"One\" for option 1 and \"Two\" for option 2. If you want sudden death, type \"Death\"]: ").strip()
        sleep(2.0)
        if random_pick_decision.upper() == "ONE":
            user_team = random_1
            print(f"\nCongratulations, you are now a member of the {user_team}.\n")
            break 
        elif random_pick_decision.upper() == "TWO":
            user_team = random_2
            print(f"\nCongratulations, you are now a member of the {user_team}.\n")
            break
        elif random_pick_decision.upper() == "DEATH":
            print("\nAn individual that likes to take risks I see.\n")
            sleep(2.0)
            while True: 
                sudden_death = uppercase_start(random.choice(nba_teams))
                if sudden_death == random_1 or sudden_death == random_2:
                    continue
                else: 
                    user_team = sudden_death
                    print(f"Congratulations, you are now a member of the {user_team}.\n")
                    break 
            break
        else:
            print("\nPlease enter either \"One\", \"Two\", or \"Death\".\n")
            continue

def team_direct_choice():
    """
    - Called within team() function based on user input
    - User directly chooses which team they would like to play on
    """
    global user_team
    print("\nAlright, taking the safe pick, understandable.\n")
    sleep(2.0)
    print("Here are your options: \n")
    sleep(2.0)
    for x in nba_teams:
        print(uppercase_start(x))
    sleep(2.0)
    while True: 
        direct_choice = input("\nNow make your choice [ENTER THE TEAM NAME AS IT IS LISTED ABOVE]: ").strip()
        sleep(2.0)
        if direct_choice.upper() not in nba_teams:
            print("\nPlease enter the team as it is listed above.")
            continue
        else:
            user_team = uppercase_start(direct_choice)
            print(f"\nCongratulations, you are now a member of the {user_team}.\n")
            break

def team():
    """
    - Starts the process of choosing an NBA team 
    - Users have two ways to do it (Direct Choice or Random/Random/Dead)
    - Based on user choice via user input, team_direct_choice or team_random_choice is called
    """
    print("Now it's time to begin your NBA journey by signing with a team!\n")
    sleep(2.0)
    print("There are two ways to do this.\n")
    sleep(2.0)
    print("Your first option is to just straight up pick what team you want to be on.\n")
    sleep(2.0)
    print("The second option is to randomize what team you get to play on.\n")
    sleep(2.0)
    print("The second option still has the element of choice as you get to choose between two randoms.\n")
    sleep(2.0)
    print("If none of the two options interest you, you can go for sudden death with one last random.\n")
    sleep(2.0)
    while True: 
        choice_ = input("What option would you like to choose? [Type \"One\" for option 1 or \"Two\" for option 2]: ").strip()
        sleep(2.0)
        if choice_.upper() == "ONE":
            team_direct_choice()
            break 
        elif choice_.upper() == "TWO":
            team_randomm_choice()
            break 
        else:
            print("\nPlease enter either \"One\" or \"Two\"\n.")
            continue

def pick_archetype():
    """
    - User chooses archetype 
    - Every position has 5 archetypes they are allowed to choose from 
    - Every archetype has 3 focused stats that relate to their playstyle
    - User will adjust focused stats in adjust_arch_stats() function
    """
    global my_player
    global user_archetype
    pg_archs = ("PLAYMAKER", "SHOT CREATOR", "SHARPSHOOTER", "SLASHER")
    sg_archs = ("LOCKDOWN", "SHOT CREATOR", "SHARPSHOOTER", "SLASHER")
    sf_archs = ("LOCKDOWN", "SHOT CREATOR", "SHARPSHOOTER", "SLASHER")
    pf_archs = ("LOCKDOWN", "POST SCORER", "SHARPSHOOTER", "SLASHER")
    c_archs = ("LOCKDOWN", "POST SCORER", "GLASS CLEANER", "SLASHER")
    print("For the final step of the MyPlayer builder, you will be choosing your archetype, and adjusting your archetypes focused stats.\n")
    sleep(2.0)
    print("In this builder, there is a combined seven different archetypes to choose from.\n")
    sleep(2.0)
    print("Every archetype has three main stats that correlate to the archetype's playstyle. We call these Focused Stats.\n")
    sleep(2.0)
    print("Here are the archetypes: \n")
    sleep(2.0)
    print('Playmaker:\nDescription: The lead floor general on the court responsible with getting his teammates involved.\n')
    print("Real Life Comparisons: Rajon Rondo, Chris Paul, Steve Nash\n")
    print("Advantages: Passing, Dribbling, Speed")
    print("Disadvantages: Shooting, Interior Defense, Finishing\n")
    print("Focused Stats: Passing Accuracy, Ball Handle, Speed with Ball\n")
    sleep(4.0)
    print('Slasher:\nDescription: Scoring oriented player that thrives in the paint.\n')
    print("Real Life Comparisons: Vince Carter, Aaron Gordon, Zach Lavine\n")
    print("Advantages: Acceleration, Driving to the basket, Finishing, Speed")
    print("Disadvantages: Shooting, Interior Defense, Playmaking\n")
    print("Focused Stats: Driving Layup, Driving Dunk, Standing Dunk\n")
    sleep(4.0)
    print('Sharpshooter:\nDescription: Scoring oriented player with a knockdown shot all around the court.\n')
    print("Real Life Comparisons: Klay Thompson, Ray Allen, Buddy Hield\n")
    print("Advantages: Shooting, Off-ball ability")
    print("Disadvantages: Defense, Finishing, Playmaking\n")
    print("Focused Stats: Free Throw, Three Pointer, Mid-Range\n")
    sleep(4.0)
    print('Lockdown:\nDescription: Defensive oriented player that loves taking the toughest matchup.\n')
    print("Real Life Comparisons: Kawhi Leonard, Gary Payton, Ben Wallace\n")
    print("Advantages: Defense, Finishing, Strength, Speed")
    print("Disadvantages: Shooting, Playmaking, Dribbling\n")
    if my_player.position  == "Center" or my_player.position  == "Power Forward" or my_player.position  == "Small Forward": 
        print("Focused Stats: Steal, Block, Interior Defense\n")
    else:
        print("Focused Stats: Steal, Block, Perimeter Defense\n")
    sleep(4.0)
    print('Shot Creator:\nDescription: Scoring oriented player with a knockdown shot all around the court.\n')
    print("Real Life Comparisons: Kobe Bryant, Jamal Crawford, Jammal Murray\n")
    print("Advantages: Mid-Range, Off-Dribble Shot")
    print("Disadvantages: Defense, Playmaking\n")
    print("Focused Stats: Post Fadeaway, Contested Shot, Off-Dribble Shot\n")
    sleep(4.0)
    print('Post Scorer:\nDescription: Scoring oriented player that loves to go down low in the post.\n')
    print("Real Life Comparisons: Hakeem Olajuwon, Joel Embiid, Nikola Jokic\n")
    print("Advantages: Mid-Range, Post Scoring, Finishing")
    print("Disadvantages: Playmaking, Speed\n")
    print("Focused Stats: Post Fadeaway, Post Hook, Post Control\n")
    sleep(4.0)
    print('Glass Cleaner:\nDescription: Hustle player that loves to get down low to grab boards and create extra opportunities.\n')
    print("Real Life Comparisons: Dennis Rodman, Adre Drummond, Bill Russel\n")
    print("Advantages: Rebounding, Interior Defense, Finishing")
    print("Disadvantages: Playmaking, Speed, Shooting\n")
    print("Focused Stats: Box Out, Offensive Rebound, Defensive Rebound\n")
    sleep(4.0)
    print("The archetypes allowed for a player are based on their position.\n")
    sleep(2.0)
    print("Here are the archetypes allowed for each position: \n")
    sleep(2.0)
    print("PG: Playmaker, Shot Creator, Sharpshooter, Slasher")
    print("SG: Lockdown, Shot Creator, Sharpshooter, Slasher")
    print("SF: Lockdown, Shot Creator, Sharpshooter, Slasher")
    print("PF: Lockdown, Post Scorer, Sharpshooter, Slasher")
    print("C: Lockdown, Post Scorer, Glass Cleaner, Slasher\n")
    sleep(2.0)
    print("If you do not enter one of the archetypes allowed for your position, you will be prompted to enter it again.\n")
    sleep(2.0)
    ready()
    arch_list = ()
    if my_player.position  == "Point Guard": 
        arch_list = pg_archs
    elif my_player.position  == "Shooting Guard": 
        arch_list = sg_archs
    elif my_player.position  == "Small Forward": 
        arch_list = sf_archs
    elif my_player.position  == "Power Forward": 
        arch_list = pf_archs
    else:
        arch_list = c_archs
    print(f'Since you are a {my_player.position}, here are your archetype options: {arch_list}.\n') 
    while True:
        user_archetype = input(f"Enter archetype here {arch_list}: ").strip()
        sleep(2.0)
        if user_archetype.upper() not in arch_list:
            print("\nPlease enter one of the listed archetypes for your position.\n")
            continue
        else:
            break

def adjust_arch_stats():
    """
    - Creates Player_archetype object for user
    - User is allowed to adjust his focused stats 
    - 3 focused stats which vary on archetype chosen by user
    - User focused stats all start as 0
    - Given 255 attribute points to spread along the 3 focused stats
    - Each focused stat has a max level of 90 
    """
    global my_player_arch
    my_player_arch = Player_archetype()
    playmaker_base = ("PASSING ACCURACY", "BALL HANDLE", "SPEED WITH BALL")
    sharp_base = ("FREE THROW", "THREE POINTER", "MID-RANGE")
    shot_base = ("POST FADEAWAY", "CONTESTED SHOT", "OFF-DRIBBLE SHOT")
    slasher_base = ("DRIVING LAYUP", "DRIVING DUNK", "STANDING DUNK")
    lock_base_back = ("STEAL", "BLOCK", "PERIMETER DEFENSE")
    lock_base_front = ("STEAL", "BLOCK", "INTERIOR DEFENSE")
    post_base = ("POST FADEAWAY", "POST HOOK", "POST CONTROL")
    glass_base = ("BOX OUT", "OFFENSIVE REBOUND", "DEFENSIVE REBOUND")

    player_base = ()

    if my_player_arch.archetype == "Playmaker":
        player_base = playmaker_base
    elif my_player_arch.archetype == "Sharpshooter":
        player_base = sharp_base
    elif my_player_arch.archetype == "Shot Creator":
        player_base = shot_base
    elif my_player_arch.archetype == "Slasher":
        player_base = slasher_base
    elif my_player_arch.archetype == "Lockdown":
        if my_player.position == "Center" or my_player.position == "Power Forward" or my_player.position == "Small Forward": 
            player_base = lock_base_front
        else:
            player_base = lock_base_back
    elif my_player_arch.archetype == "Post Scorer":
            player_base = post_base
    else:
        player_base = glass_base
    print("\nWelcome to the final step of the MyPlayer builder. Here, you will be adjusting your focused stats.\n")
    sleep(2.0)
    print("In this builder, every archetype has 3 focused stats that correlate to the archetype's playstyle.\n")
    sleep(2.0)
    print("For a quick reminder, here are the focused stats for each archetype.\n")
    sleep(2.0)
    print("Playmaker: Passing Accuracy, Ball Handle, Speed with Ball")
    print("Slasher: Driving Layup, Driving Dunk, Standing Dunk")
    print("Sharpshooter: Free Throw, Three Pointer, Mid-Range")
    if my_player.position == "Center" or my_player.position == "Power Forward" or my_player.position == "Small Forward": 
        print("Lockdown: Steal, Block, Interior Defense")
    else:
        print("Lockdown: Steal, Block, Perimeter Defense")
    print("Shot Creator: Post Fadeaway, Contested Shot, Off-Dribble Shot")
    print("Post Scorer: Post Fadeaway, Post Hook, Post Control")
    print("Glass Cleaner: Box Out, Offensive Rebound, Defensive Rebound\n")
    sleep(2.0)
    print(f"Currently, as a {my_player_arch.archetype} every one of your focused stats are set to zero.\n")
    sleep(2.0)
    print(my_player_arch)
    sleep(2.0)
    print("You will get 255 points to spend across your stats. Again, we call these Attribute Points.\n")
    sleep(2.0)
    print("You cannot go over the assigned 255 attribute points or make it negative.\n")
    sleep(2.0)
    print("In addition, every focused stat has a max level of 90. However, not every stat can be afforded to be at max level.\n")
    sleep(2.0)
    print(f"In your case, as a {my_player_arch.archetype}, these are the max levels for you focused stats.\n")
    sleep(2.0)
    my_player_arch.print_maxes() 
    sleep(2.0)
    print("Throughout the process, if you are done with adjusting your stats, simply type \"Done\" for any of the prompts.\n")
    sleep(2.0)
    ready()
    while True:
        try: 
            attribute_change = input(f"Attribute to change? {player_base}: ").strip()
            if attribute_change.upper() == "DONE":
                if leave_or_stay(my_player_arch.attr_points, "Archetype") == True:
                    break
                else:
                    continue 
            if attribute_change.isnumeric() ==  True:
                raise ValueError
            if attribute_change.upper() not in player_base and attribute_change.upper() != "DONE":
                raise TypeError
        except ValueError:
            print(f"\nSorry, we couldn't process that request. Please enter one of these 3 Focused stats {player_base} or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except TypeError:
            print(f"\nSorry, we couldn't process that request. Please enter one of these 3 Focused stats {player_base} or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except:
            print(f"\nSorry, we couldn't process that request. Please enter one of these 3 Focused stats {player_base} or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        
        try:
            type_change = input("\nEnter \"I\" if you want to increase a stat, or \"D\" if you want to decrease a stat: ").strip()
            if type_change.upper() == "DONE":
                if leave_or_stay(my_player_arch.attr_points, "Archetype") == True:
                    break
                else:
                    continue
            if type_change.isnumeric() ==  True:
                raise ValueError
            if type_change.upper() != "I" and type_change.upper() != "D" and type_change.upper() != "DONE":
                raise TypeError
        except ValueError:
            print("\nSorry, we couldn't process that request. Please enter either \"I\" to increase the stat or \"D\" to decrease the stat or just \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except TypeError:
            print("\nSorry, we couldn't process that request. Please enter either \"I\" to increase the stat or \"D\" to decrease the stat or just \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except:
            print("\nSorry, we couldn't process that request. Please enter either \"I\" to increase the stat or \"D\" to decrease the stat or just \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
    
        try:
            value_change = input(f"\nBy how much would you like to make this change? [{my_player_arch.stat_status(attribute_change.upper())}]: ").strip()#figure out a way for user to exit from here 
            if value_change.upper() == "DONE":
                if leave_or_stay(my_player_arch.attr_points, "Archetype") == True:
                    break
                else:
                    continue
            if value_change.upper() != "DONE" and value_change.isalpha() ==  True:
                raise ValueError
        except ValueError:
            print("\nSorry, we couldn't process that request. Please enter either a number to increase of decrease the stat or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        except:
            print("\nSorry, we couldn't process that request. Please enter either a number to increase of decrease the stat or \"Done\".\n")
            sleep(2.0)
            print("We will start over.\n")
            sleep(2.0)
            continue
        print("")
    
        if attribute_change.upper() == "BALL HANDLE":
            my_player_arch.ball_handle_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "SPEED WITH BALL":
            my_player_arch.speed_with_ball_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "PASSING ACCURACY":
            my_player_arch.pass_accuracy_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "THREE POINTER":
            my_player_arch.three_point_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "MID-RANGE":
            my_player_arch.mid_range_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "FREE THROW":
            my_player_arch.free_throw_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "DRIVING DUNK":
            my_player_arch.driving_dunk_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "DRIVING LAYUP":
            my_player_arch.driving_layup_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "STANDING DUNK":
            my_player_arch.standing_dunk_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "OFF-DRIBBLE SHOT":
            my_player_arch.off_dribble_shot_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "CONTESTED SHOT":
            my_player_arch.contested_shot_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "POST FADEAWAY":
            my_player_arch.post_fadeaway_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "PERIMETER DEFENSE":
            my_player_arch.perimeter_defense_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "INTERIOR DEFENSE":
            my_player_arch.interior_defense_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "STEAL":
            my_player_arch.steal_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "BLOCK":
            my_player_arch.block_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "POST CONTROL":
            my_player_arch.post_control_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "POST HOOK":
            my_player_arch.post_hook_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "BOX OUT":
            my_player_arch.box_out_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "OFFENSIVE REBOUND":
            my_player_arch.offensive_rebound_change(type_change.upper(),int(value_change))
        elif attribute_change.upper() == "DEFENSIVE REBOUND":
            my_player_arch.defensive_rebound_change(type_change.upper(),int(value_change))
        
        print("Here are your current stats: \n")
        sleep(2.0)
        print(my_player_arch)
        sleep(2.0)
        print(f"Current Attribute Points Used: {my_player_arch.attr_points}.\n")
        print(f"Current Attribute Points left: {255 - my_player_arch.attr_points}.\n")

def final_results(user_name, user_team, user_college, user_position, user_jersey_number, user_height, user_archetype):
    """
    - Relays final results of the MyPlayer builder process 
    """
    global my_player
    global my_player_arch
    print("\nCongratulations, you have completed the my player process!\n")
    sleep(2.0)
    print("Here are your results!\n")
    sleep(2.0)
    print(f"Name: {user_name}")
    print(f"Team: {user_team}")
    print(f"College: {user_college}")
    print(f"Jersey #: {user_jersey_number}")
    print(f"Height: {user_height}\n")
    sleep(2.0)
    print(my_player)
    sleep(2.0)
    print(my_player_arch)




intro()
sleep(5.0)
position()
sleep(3.0)
adjust_base_stats()
sleep(2.0)
height()
college()
sleep(5.0)
team()
sleep(5.0)
jersey_number()
sleep(5.0)
pick_archetype()
sleep(5.0)
adjust_arch_stats()
sleep(5.0)
final_results(user_name, user_team, user_college, my_player.position, user_jersey_number, user_height, my_player_arch.archetype)



