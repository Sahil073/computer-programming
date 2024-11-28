'''The Superhero Names Game'''
def name_editior(names):
    l = []
    for i in names:
        first, lname = i.split()
        super_name = first[0] + "." + lname
        l.append(super_name)
    return l    
print(*name_editior(eval(input())))

