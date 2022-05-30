def cipher(text,gap,direction):
    print("Text to encode is: %s" % text )
    word=list(text)
    if direction=="decoding":
        gap*=-1
    for i in range(len(text)):
        if word[i]==" ":
            word[i]=" "
        elif int(ord(word[i]))+gap<122 and ord(word[i])+gap>96:
            word[i]=chr(ord(word[i])+gap)
        elif ord(word[i])+gap>123:
            word[i]=chr(ord(word[i])+gap-26)
        elif ord(word[i])+gap<96:
            word[i]=chr(ord(word[i])+gap+26)
        
            
    
    return ''.join(word)
    
texts=input('Input text to encode \n').lower()
gap=int(input("Input letters gap \n"))
direction=input("Choose direction encoding/decoding \n")
print("Encoding message %s " % cipher(texts,gap,direction))
print("Decoding message %s " % cipher(texts,gap,"decoding"))

