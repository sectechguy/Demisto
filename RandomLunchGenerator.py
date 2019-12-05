'''
Lunch Script 3.0
This script randomly selects a themed lunch then selects a rest from that list
'''

import random

food_lists = {
    "Pizza List": ['Chuck E. Cheese','Target Pizza Hut',"Antonio's Pizza",'Romeos Pizza','Little Caesars',"Papa John's",'Dominos',"Pavona's Pizza Joint","Rocco's Pizza Shop","Teresa's Pizza","Mr. G's"],
    "Sandwich List": ['Subway','Jersey Mikes','Penn Station','Firehouse Subs','The Sub Station','Magic Subs & Gyros',"Mr. Zub's Deli", 'Corral Sanwich Shop','Hanini Subs',"Jimmy John's"],
    "Mexican List": ['Taco Bell','Funky Truckeria','Chipotle',"Tito's Mexican Grill",'Tres Potrillos','El Rancho',"Moe's Southwest Grill",'BOMBA Tacos','Qdoba','Casa Del Rio'],
    "Burger List": ['Wayback','The Rail','Five Guys',"Louie's Bar & Grille","Bob's Hamburg",'Swensons',"Rally's",'Skyway',"Hodge's Cafe","Wendy's",'Burger King',"McDonald's"],
    "Healthy List": ['First Watch',"Ms. Julie's Kitchen",'Continental Cuisine',"Niko's Sandwich Board",'Poke Fresh','Zoup!',"Aladdin's Eatery","Beau's Grille",'Valley Cafe','CoreLife Eatery'],
    "Sit Down List": ["Friday's",'Red Lobster','Olive Garden',"Applebee's","P.F. Chang's","Rockne's Restaurant",'Akron Family Restaurant','BRAVO','Cracker Barrel','Wally Waffle','Kingfish',"Ken Stewart's Grille",'Long Horn','Lockkeepers','Bonefish Grille'],
    "Asian List": ['China King','Imperial Wok','China Star','Platinum Dragon','Sushi Asia Gormet','China Express','New Ming Restaurant','House of Hunan','Sushi Katsu','Sakura','T J Sushi','Big Eye Japanese Cuisine & Sushi Bar','Hong Kong Buffet','Taste of Bankok','Hyde Out']}

category=random.choice(list(food_lists.keys()))
restaurant=random.choice(food_lists[category])
print(category)
print(restaurant)
