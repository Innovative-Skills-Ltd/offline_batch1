product_name =['shirt','pant','panjabi']

print(len(product_name))

#index based loop

for i in range(0,len(product_name)):
    print(product_name[i])

#value based loop

product_name.append('tupi')

product_name = product_name + ['x','y']

for i in range(10):
    new_value = input("Enter")
    product_name = product_name + [new_value]

print(product_name)

# for i in product_name:
#     print(i)


