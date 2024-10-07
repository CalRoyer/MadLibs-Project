'''
Cal Royer
10/6/24
'''

print("Welcome to this MadLibs Game!".center(60,"-"))

# Name and Date
name = input("What is your name?")
print(name.title())
date = input("What is todays date? (ex: dd/mm/yy)")
print(date)

# User Input
verb1 = str(input("Pick a verb:"))
adjective1 = str(input("Pick an adjective:"))
noun1 = str(input("Pick a noun:"))
verb2 = str(input("Pick another verb:"))
adverb1 = str(input("Pick an adverb:"))
adjective2 = str(input("Pick another adjective:"))
noun2 = str(input("Pick another noun:")) 
verb3 = str(input("Pick a third verb:"))
adverb2 = str(input("Pick a second adverb:"))
adjective3 = str(input("Pick a third adjective:"))
noun3 = str(input("Pick a third noun:"))
verb4 = str(input("Pick a fourth verb:"))
verb5 = str(input("Pick a final verb:"))
noun4 = str(input("Pick a fourth noun:"))
noun5 = str(input("Pick a final noun:"))

# Story Output
print(f"""It was a beautiful day on {date}, {name} decided it was the perfect day for an adventure. 
The weather was just right for {verb1}. Along the way, they came across a {adjective1} {noun1} and decided to {verb2} with it. 
The {noun1} was {adverb1} moving around, but {name} found it fascinating.
Later, {name} found a group of {adjective2} {noun2}s and joined them in a fun game of {verb3}. 
They were {adverb2} enjoying themselves when suddenly, a {adjective3} {noun3} appeared out of nowhere! 
Everyone quickly {verb4}, and after some excitement, they all decided to {verb5} by the {noun4}.
As the sun began to set, {name} reflected on the adventure, knowing that the memory of this {noun5} would last forever.""") 