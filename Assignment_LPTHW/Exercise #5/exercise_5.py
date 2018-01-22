my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180 # lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'
his_prison_record = ' manslaughter'
years = '25'
get_out = 'never'
his_type = 'doppelganger'
true_self = 'a convicted felon'
his_name = 'Joe Jonas'
print("Let's talk about {my_name}".format(**locals()))
print("He's {my_height} inches tall.".format(**locals()))
print(" He's {my_weight} pounds heavy.".format(**locals()))
print(" Actually, he's not that heavy.")
print("He's got {my_eyes} eyes and {my_hair} hair.".format(**locals()))
print("His teeth are usually {my_teeth} depending on the coffee.".format(**locals()))
print("He is not me. He is a {his_type}.".format(**locals()))
print(f"Oh no! And I just found out he is a {true_self} who has served {years} years.")
print(f"He is supposed {get_out} get out!.")
print(f"He is really {his_name}!Serving a {his_prison_record} sentence!")
# this line is tricky to get it exactly right
total = my_age + my_height + my_weight
print("If I add {my_age}, {my_height}, and {my_weight} I get {total}.".format(**locals()))
