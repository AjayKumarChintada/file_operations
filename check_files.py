def write_file(filename,data:str):
    with open(filename,'a') as file:
        file.write(str(data)+'\n')


def check_exist(filename,flag):
    with open(filename,'r') as file:
        data = file.readlines()
        data = [i.strip() for i in data]
        print(data)
        for i in data:
            if i==flag:
                return 1

    return 0


a = [1,2,34]

filename = 'laptops.txt'
for i in a:
    data = open(filename)
    laptop_data = data.readlines()
    laptop_data = [i.strip() for i in laptop_data]
    if check_exist(filename,i):
        continue
    write_file(filename,i)



