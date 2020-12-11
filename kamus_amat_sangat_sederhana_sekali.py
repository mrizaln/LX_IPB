kam = {'aku':'I','saya':'I','kamu':'you','dia':'he','mereka':'they','kita':'we','kami':'we'}

kalst = input()
kalen = ''.join((kam.get(ele,ele) + ' ') for ele in kalst.split()).strip()

print(kalen, end = '\n')
