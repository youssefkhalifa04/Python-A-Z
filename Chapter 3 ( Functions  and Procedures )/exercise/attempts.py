
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


def starting_position (ch1 , ch2) :
    if ch1 in ch2 :
        return ch2.index(ch1)
    else :
        return -1

def longtitude (ch) :
    if "lon" not in ch : 
        return -1
    
    c = ""
    counter = 0
    for i in range(starting_position("lon", ch) + 3, len(ch)) :
        if ch[i] in "0123456789"  or ch[i] == "." :
            c += ch[i]
        elif ch[i] == '"' :
            counter += 1
            if counter == 2 :
                break

    return float(c)
    
    

test = '   <   trkpt lat=    "257" lon="3.123456">'


print ("longtitude: ", longtitude(test))






def latitude (ch) :
    l = ch.split('"')
    return float(l[1])

print ("latitude: ", latitude(test))



