#TODO: Create a letter using starting_letter.txt
content = []
names = []
with open("./Input/Letters/starting_letter.txt", mode='r') as template:
    content = template.readlines()

with open("./Input/Names/invited_names.txt", mode='r') as person:
    names = person.readlines()

for name in names:
    with open(f"./Output/ReadyToSend/Letter_to_{name}.txt", mode='w') as output:
        for line in content:
            res = line
            if(res.__contains__("[name]")):
                res = res.replace("[name],", f"{name.strip()},")
            if(res.__contains__("Angela")):
                res = res.replace("Angela", "Akash")
            output.write(res)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp