

def read_file (filename) :
    with open ( filename , "r"  ) as f :
        lines = []
        for line in f :
            lines.append(line.strip())
            
    return lines


def convert (lines) :
    
    new = []
    person = None
    for line in lines :
        if line == 'Miko' :  
            person = 'Miko'
            continue
        elif line == 'Leo' : #到leo 會取代
            person = 'Leo'
            continue
    if person :
        new.append(person + ': ' + line)   #要在loop裡面 不然會迭代  
    return new
    

def write_file(filename , lines) :
    with open (filename , 'w' ,encoding='utf-8') as f :
        for line in lines :
            f.write(line + '\n')


def main() :
    lines = read_file('input.txt')
    convert(lines)
    write_file('output.txt' ,lines)

main()