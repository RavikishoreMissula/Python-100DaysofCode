# Higher and Lower Game

import random

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social Media Platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Singer and Dancer',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Jhonson',
        'follower_count': 181,
        'description': 'Actor and Professional Wrestler',
        'country': 'United States'
    },
    {
        'name': 'Donald Trump',
        'follower_count': 346,
        'description': 'President of United States',
        'country': 'United States'
    },
    {
        'name': 'Narendra Modi',
        'follower_count': 500,
        'description': 'Prime Minister of India',
        'country': 'India'
    },
    {
        'name': 'Mahendra Singh Dhoni',
        'follower_count': 777,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Twitter',
        'follower_count': 444,
        'description': 'Social Media Platform',
        'country': 'United States'
    },
    {
        'name': 'Angela Yu',
        'follower_count': 567,
        'description': 'Trainer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Ravikishore',
        'follower_count': 123,
        'description': 'IT Employee',
        'country': 'India'
    },
    {
        'name': 'Ramya',
        'follower_count': 999,
        'description': 'Social Media Influencer',
        'country': 'India'
    },
    {
        'name': 'Rasya',
        'follower_count': 1111,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Shahrukh Khan',
        'follower_count': 234,
        'description': 'Actor',
        'country': 'India'
    }
]

game_logo = ('''
 __    __   __    _______  __    __   _______ .______        
|  |  |  | |  |  /  _____||  |  |  | |   ____||   _  \       
|  |__|  | |  | |  |  __  |  |__|  | |  |__   |  |_)  |      
|   __   | |  | |  | |_ | |   __   | |   __|  |      /       
|  |  |  | |  | |  |__| | |  |  |  | |  |____ |  |\  \----.  
|__|  |__| |__|  \______| |__|  |__| |_______|| _| `._____|  

 __        ______   ____    __    ____  _______ .______      
|  |      /  __  \  \   \  /  \  /   / |   ____||   _  \     
|  |     |  |  |  |  \   \/    \/   /  |  |__   |  |_)  |    
|  |     |  |  |  |   \            /   |   __|  |      /     
|  `----.|  `--'  |    \    /\    /    |  |____ |  |\  \----.
|_______| \______/      \__/  \__/     |_______|| _| `._____|

''')

vs = ('''
____    ____   _______.
\   \  /   /  /       |
 \   \/   /  |   (----`
  \      /    \   \    
   \    / .----)   |   
    \__/  |_______/    

''')

score = 0
play_game = True

while play_game:
    print(game_logo)
    a = random.choice(data)
    b = random.choice(data)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (answer == 'a' and a['follower_count'] > b['follower_count']) or (
            answer == 'b' and b['follower_count'] > a['follower_count']):
        score += 1
        print(f"You're Right! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        play_game = False