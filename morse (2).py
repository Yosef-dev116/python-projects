#section 2
'''Group members:
    - Yeabsira Anteneh(UGR/SWE/0113/22)
    - Suraphel Nega(BITS/UGR/0162/24)
    - Mohammed Temam(UGR/0148/24)
    - Nebeyu Essayas(BITS/UGR/0156/24)'''


import winsound

morse ={"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".—", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", 
    "0": "—–", "1": ".—-", "2": "..—", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "—..", "9": "—-."}

def encode(): #convert text to morse
    text_to_encode = input("Enter text to encode or type 'quit' to quit: ").upper()#accept text input from user 
    if text_to_encode == 'quit':
        quit()
    else:
        for text in text_to_encode: #iterate through each letters of the input text
            if text != ' ': #check if there is a space in the input text
                encoded_txt = morse.get(text) #if there's no space get the corresponding morse code
            else:
                encoded_txt = ' ' #if there's a space print it out 
            print(encoded_txt, end=" ")
            
   
        ask_sound = input("\nDo you want to play sound?(y/n): ").lower() #ask user if they want to play sound

        if ask_sound == 'y':
            for char in encoded_txt: #if yes, iterate through the morse code from above
                if char == '.': 
                    winsound.Beep(1000, 1000) #if '.' is found, play a beep sound of frequency 1000Hz for 1000 milliseconds
                elif char == ' ':
                    winsound.Beep(0,50) #if a space is found, remain silent for 50 milliseconds
                elif char == '-':
                    winsound.Beep(1000, 1500) #if '-' is found, play a beep sound of frequency 1000Hz for 1500 milliseconds
                    
        else: #if no, exit
            print('sound omitted')


def decode(): #convert morse to text
    decode = {v:k for k, v in morse.items()} #inverse the key : value order to value : key in the above morse dictionary
    text_to_decode = input("\nEnter morse code to decode where each morse is separated by a space, if you want to add space between decoded characters use '//', use 'quit' to quit: ") #accept morse input
    if text_to_decode == 'quit':
        quit()
    else:
        decode_morse = text_to_decode.split() #separate each morse code whenever a space is found and form a list of morse code strings
        for text in decode_morse: 
            if text != '//': 
                x = decode.get(text) 
            else:
                x = ' ' #if '//' is found, use it as a separator. This is because we can't use ' '(space) as a separator between characters as we use 'split' whenever there's a space.
            print(x, end="")
            



while True:
    ask = input("\nDo you want to encode or decode?(e/d). Press 'q' to quit: ").lower()
    if ask == 'q':
        quit()
    elif ask == 'e':
        encode()
    elif ask == 'd':
        decode()
    else:
        print('Invalid option')
        continue

