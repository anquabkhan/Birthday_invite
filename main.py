#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
print("KASK")
print('k')
print('j')
with open('./input/letters/starting_letter.txt', mode='r') as file:
        # con = file.read()
        # print(file.readable())
        # print(con)
        print(f"the new line is")
        c2 =  file.read()
        c3 = c2.replace('[name]', 'Anquab')
        print(c3)
        i = 0
        with open('./input/Names/invited_names.txt') as f_name:
                for line in f_name:
                        line2 = line.strip()
                        i += 1
                        c3 = c2.replace('[name]', line2)
                        print(c3)
                        with open(f'./output/ReadyToSend/new_file{i}.txt', mode='x') as f:
                                 f.write(c3)
        #     # for line in f:
        #     #    f.write(line.replace(__old='[name]', __new='anquab'))
        #     cont = f.read()
        #     print(cont)
        #     line.replace('anquab')
        #     f.write(line)

# print('Hi')




