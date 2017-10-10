productCatalog = {"Pencil":2,"Pen":10,"Eraser":3,"Ruler":10,"Sharpener":2}
input = input("Enter product name : ")
print(productCatalog[input])
if(input in productCatalog):
    print(productCatalog.get(input))
else:
    print('Product Not Found')