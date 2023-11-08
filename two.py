#192.168.128.1
# def validate_ip(ip):
#     param = ip.split('.')
#     pierwsza_kropka = param[0].isnumeric() 
#     if len(param[0])!=3:
#         return False
#     druga_kropka = param[1].isnumeric()
#     if len(param[1])!=3:
#         return False
#     trzecia_kropka = param[2].isnumeric()
#     if len(param[2])!=3:
#         return False
#     czwarta_kropka = param[3].isnumeric()
#     if len(param[3])!=1:
#         return False
#     return pierwsza_kropka and druga_kropka and trzecia_kropka and czwarta_kropka
    
# if validate_ip("192.168.128.1"):
#     print("T")
# else:
#     print ("N")

def validate_ip(ip):
    param = ip.split('.')
    for i in range(4):
        if param[i].isnumeric():
            return True
        else: 
            return False
    
if validate_ip("192.168.128.1"):
    print("T")
else:
    print ("N")
