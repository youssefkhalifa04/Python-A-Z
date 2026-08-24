
m1 = "montag"
m2 = "efmond"



def get_index (a , mot):
    for i in range(0, len(mot)):
        if mot[i] == a :
            return i


def pr (m1 , m2):
    l = []
    
    a = 0
    b = 0 
    
    for i in range(0,len(m1)) :
        x = ""
        y = ""
        if m1[i] in m2 :
            b = get_index(a = m1[i], mot = m2)
            a = i
            x = m1[a]
            y = m2[b]
            while True : 
                
                a += 1
                b+= 1
                f = x + m1[a]
                g = y + m2[b]
                if f != g :
                    break
                x +=  m1[a]
                y += m2[b]
            print("x : ", x)
            print("y : ", y)
            if x == y and len(x) >= 2 :
                l.append(x)
       
    return max(l , key = len)

print("the longest common substring is: ", pr(m1, m2))



        
