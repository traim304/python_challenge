#库的官方文档: https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy.system.listMethods


import xmlrpc.client

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
ServerProxy = xmlrpc.client.ServerProxy(url)
#列出能够调用的所有方法
all_methods = ServerProxy.system.listMethods()

print("All methods under there:")
for i in range(len(all_methods)):
    print('    ' + all_methods[i])

#调用 phone 方法 参数为上一关的 readme.txt 中的 Bert
print("Now Phone that guys --> Bert")
print(ServerProxy.phone('Bert'))

print("\nSo:    " + "http://www.pythonchallenge.com/pc/return/italy.html")