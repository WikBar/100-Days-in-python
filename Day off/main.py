if __name__ == '__main__':
    x = 2
    y = 2
    z = 2
    n = 3
    
    l=[[x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1) if x1+y1+z1!=n] 
    
    print(l)