# supplied variables for child array

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

# Define Four Python Functions

def run(childArray):
    for child in childArray:
        print(f'{child} ran like hell!!!')
        
run(running_kids)
        
def swing(childArray):
    for child in childArray:
        print(f'{child} is swinging for the fences!!!')
        
swing(swinging_kids)

def slide(childArray):
    for child in childArray:
        print(f'{child} is sliding like a maniac!!!')
        
slide(sliding_kids)

def hide_and_seek(childArray):
    for child in childArray:
        print(f'{child} is playing hide and seek so metal!!!')
        
hide_and_seek(hiding_kids)

# Chicken Monkey Practice

def chicken_monkey():
    
    for unit in range(1, 101):
        is_chicken_monkey = False
        print(unit)
        if unit % 5 == 0 and unit % 7 == 0:
            print(f'{unit} is Chicken Monkey Tacos')
            is_chicken_monkey = True
        if is_chicken_monkey == False:
            if unit % 5 == 0:
                print(f'{unit} it is a chicken!')
            if unit % 7 == 0:
                print(f'{unit} it is a monkey!')
                
chicken_monkey()

# fin monkey has been chickened to tacos
