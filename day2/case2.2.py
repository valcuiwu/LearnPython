products = []
with open ('a.txt','r',encoding='utf-8') as file:
    for i in file.readlines():
        products.append(i.strip().split())
        # print(products)
        for j in products:
            print(int(j[1])*int(j[2]))