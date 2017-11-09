import os  # 代表操作系统
import sys # 代表python系统
import csv
#print(sys.path)

#print(os.getcwd())
#
#size = 0
#try:
#    size = os.path.getsize(r'D:\workspace\test\day5\ssff.txt')
#except FileNotFoundError as e:
#    print(e)
#
#print(size)
def write_to_csv(filename, mode, rows):
    with open(filename, mode, newline='') as jobs:
        writer = csv.writer(jobs)
        if mode == 'w':
            writer.writerow(('职位名','公司'))
        writer.writerows(rows)

def write_to_csv_auto(filename, rows):

    #path = os.getcwd() + '\\' + filename #
    path = ''.join([os.getcwd(), '\\', filename])
    print(path)
    size = 0
    try:
        size = os.path.getsize(path)
    except FileNotFoundError as e:
        print(e)
    
    if size == 0:
        write_to_csv(filename, 'w', rows)
    else:
        write_to_csv(filename, 'a', rows)
    

if __name__ == '__main__':
    rows = [('pythonkaifa', '公司名'),('java', '百度')]
    write_to_csv_auto('tmp.csv', rows)