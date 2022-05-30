def encode(text,gap):
    print("Text to encode is: %s" % text )
    word=list(text)
    
    for i in range(len(text)):
        if word[i]==" ":
            word[i]=" "
        elif int(ord(word[i]))+gap<123 and ord(word[i])+gap>96:
            word[i]=chr(ord(word[i])+gap)
        elif ord(word[i])+gap>123:
            word[i]=chr(ord(word[i])+gap-26)
        elif ord(word[i])+gap<96:
            word[i]=chr(ord(word[i])+gap+26)
        
            
    
    return ''.join(word)
    
def decode(text,gap):
    
    print(f"Text to decode is: {text}")
    word=list(text)
    
    for i in range(len(text)):
        if word[i]==" ":
            continue
        elif int(ord(word[i]))-gap<123 and ord(word[i])-gap>96:
            word[i]=chr(ord(word[i])-gap)
        elif ord(word[i])-gap<96:
            word[i]=chr(ord(word[i])-gap+26)
        elif ord(word[i])-gap>123:
            word[i]=chr(ord(word[i])-gap-26)

    return "".join(word)

texts=input('Input text to encode ').lower()
gap=int(input("Input letters gap "))

print("Encoding message %s " % encode(texts,gap))
print("Decoding message %s " % decode(encode(texts,gap),gap))

