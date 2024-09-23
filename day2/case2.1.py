# 初始化商品列表
products = []

# 读取文件并构建商品列表
with open('a.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # 去除行首尾空白并分割
        parts = line.strip().split()
        if len(parts) == 3:  # 确保有三个部分
            product = {
                'name': parts[0],
                'price': int(parts[1]),  # 转换为整数
                'amount': int(parts[2])   # 转换为整数
            }
            products.append(product)

# 输出商品列表
print("商品列表", products)

total_price = 0
# 计算总价
for i in products:
    total_price += i['price'] * i['amount']

# 输出总价
print("总价:", total_price)

# Output:
[{'name': 'apple', 'price': 10, 'amount': 3}, {'name': 'tesla', 'price': 100000, 'amount': 1}, {'name': 'mac', 'price': 3000, 'amount': 2}, {'name': 'lenovo', 'price': 30000, 'amount': 3}, {'name': 'chicken', 'price': 10, 'amount': 3}]
总价: 196060