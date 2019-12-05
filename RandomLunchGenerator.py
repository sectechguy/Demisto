'''
Lunch Script 2.0
This script randomly selects a themed lunch suggestion based off of the day of week
'''

import random
import datetime
from datetime import date

if str(date.today()) == '2019-12-01':
    lunch_list=['Eat Primanti Brothers Sandwiches At Heinz Field While Watching The Steelers Allow Only One Browns Touchdown And Sack Mayfield 5 Times']
elif datetime.datetime.today().weekday() == 0:
    lunch_list=['Chuck E. Cheese','Target Pizza Hut',"Antonio's Pizza",'Romeos Pizza','Little Caesars',"Papa John's",'Dominos',"Pavona's Pizza Joint","Rocco's Pizza Shop","Teresa's Pizza","Mr. G's"]
elif datetime.datetime.today().weekday() == 1:
    lunch_list=['Subway','Jersey Mikes','Penn Station','Firehouse Subs','The Sub Station','Magic Subs & Gyros',"Mr. Zub's Deli", 'Corral Sanwich Shop','Hanini Subs',"Jimmy John's"]
elif datetime.datetime.today().weekday() == 2:
    lunch_list=['Taco Bell','Funky Truckeria','Chipotle',"Tito's Mexican Grill",'Tres Potrillos','El Rancho',"Moe's Southwest Grill",'BOMBA Tacos','Qdoba','Casa Del Rio']
elif datetime.datetime.today().weekday() == 3:
    lunch_list=['Wayback','The Rail','Five Guys',"Louie's Bar & Grille","Bob's Hamburg",'Swensons',"Rally's",'Skyway',"Hodge's Cafe","Wendy's",'Burger King',"McDonald's"]
elif datetime.datetime.today().weekday() == 4:
    lunch_list=['First Watch',"Ms. Julie's Kitchen",'Continental Cuisine',"Niko's Sandwich Board",'Poke Fresh','Zoup!',"Aladdin's Eatery","Beau's Grille",'Valley Cafe','CoreLife Eatery']
elif datetime.datetime.today().weekday() == 5:
    lunch_list=["Friday's",'Red Lobster','Olive Garden',"Applebee's","P.F. Chang's","Rockne's Restaurant",'Akron Family Restaurant','BRAVO','Cracker Barrel','Wally Waffle','Kingfish',"Ken Stewart's Grille",'Long Horn','Lockkeepers','Bonefish Grille']
else:
    lunch_list=['China King','Imperial Wok','China Star','Platinum Dragon','Sushi Asia Gormet','China Express','New Ming Restaurant','House of Hunan','Sushi Katsu','Sakura','T J Sushi','Big Eye Japanese Cuisine & Sushi Bar','Hong Kong Buffet','Taste of Bankok','Hyde Out']

lunchview_list=random.choice(lunch_list)
print (lunchview_list)
