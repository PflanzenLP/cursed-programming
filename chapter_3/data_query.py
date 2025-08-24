def read_file():
    accepted = False
    while not accepted:
        accepted = True
        file_input = input("What is the name of the file you want to read?\n")
        try:
            file = open(file_input, "r")
        except:
            print("There is no such file. Try another.")
            accepted = False
    
    split_input = file.read().split()
    input_dict = {}
    for x in split_input:
        try:
            input_dict[x.lower()] += 1
        except:
            # another cursed implementation using try-except:
            # default values for dictionary entries
            input_dict[x.lower()] = 1
    return input_dict

with open("counted_words.txt", "w") as out_file:
    # this was the one-liner I handed in
    out_file.write("\n".join(f"{key}: {value}" for key, value in sorted(read_file().items(), key=lambda item: item[1], reverse=True)))