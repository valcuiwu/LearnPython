products = []

with open ('a.txt','r',encoding='utf-8') as file:

    ni = 0
    nj = 0
    total_price = 0

    for i in file.readlines():
        products.append(i.strip().split())
        print(products)
        print('i1=',i)
        ni += 1
        print('ni=',ni,'nj=',nj)
        print('-----------')

        for j in products:
            print(int(j[1])*int(j[2]))
            print('i2=', i)
            print('j2=',j)
            nj += 1
            print('ni=', ni, 'nj=', nj)
            print('**************')
            if  (ni == 1 and nj == 1)or\
                (ni == 2 and nj == 3)or \
                (ni == 3 and nj == 6)or \
                (ni == 4 and nj == 10)or \
                (ni == 5 and nj == 15):
                price = int(j[1])*int(j[2])
                total_price = total_price + price
                print(int(j[1])*int(j[2]))
                print('================')
    print('总价:',total_price)