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