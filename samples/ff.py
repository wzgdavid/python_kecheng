
with open(r'd:\entry_points.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line.decode('utf-8')
        #print(line)