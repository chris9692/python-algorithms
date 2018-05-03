def permute(chars, p):
    if(len(chars) == p):
        print(''.join(chars))
    else:
        for i in range(p, len(chars)):
            temp = chars[i]
            chars[i] = chars[p]
            chars[p] = temp
            permute(chars, p + 1)
            temp = chars[i]
            chars[i] = chars[p]
            chars[p] = temp

if __name__ == '__main__':
    permute(list("cat"), 0)        
