#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list = []
file = open("Input/Letters/starting_letter.txt")
content = file.read()
with open("Input/Names/invited_names.txt") as f:
    while True:
        line = f.readline()
        if not line:  # Check if the line is empty (end of file)
            break
        # Process the line here
        name_list.append(line.strip())
    for name in name_list:
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode='w') as f2:
            new_content  = content.replace("[name]", f"{name}")
            f2.write(new_content)



