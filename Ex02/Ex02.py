character = "a"
character1 = "z" 

#find unicode of a
unicode_char = ord(character)
print (unicode_char) 

#find unicode of z
unicode_char = ord(character1)
print (unicode_char) 

for x in range(97,123):
    letter = chr(x)
    alphabet = "" + letter
    print (alphabet)

    def alphabet ():
        for i in range (ord('a'), ord ('z') +1):
            print (chr(i))

            alphabet()