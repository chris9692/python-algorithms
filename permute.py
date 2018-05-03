def permute(chars, p):
    if(len(chars) == p):
        print(''.join(chars))
    else:
        for i in range(p, len(chars)):
            
            #move data at position i to position p
            chars[i], chars[p] = chars[p], chars[i]
            
            permute(chars, p + 1)
            
            #switch back data at position i and p
            chars[i], chars[p] = chars[p], chars[i]

if __name__ == '__main__':
    permute(list("cat"), 0)        
