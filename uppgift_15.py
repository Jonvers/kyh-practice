#text = input("Lägg till text här:")
#print(f"{text}")
#counter=len(text.split())
#print(str(counter))
#print ("antal ord " + str(counter))

#def vowel_counter(char):
   # if char.lower() ==  "a" or char.lower() == "i" or char.lower() == "e" or char.lower() == "o" or char.lower() == "u":
        #print (char)
        #return True
#def main():
    #counter = 0
    #text = input("Ange text:")
    #for char in text:
        #if vowel_counter(char):
            #counter = counter +1
    #print(counter)

#if __name__ == '__main__':
    #main()

runners_in_order = ('Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus'.split())
vem = input('Ange löpare du söker placering för')
placering =0
for runner in runners_in_order:
    placering= placering +1
    if vem == runner:
        print(f"{runner} hamnade på {placering} plats")