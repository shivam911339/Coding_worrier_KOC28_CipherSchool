cl = {'vishal': 4569231452, 'bala': 6154651652,
      "pankaj": 2581963470, 'yogesh': 3569821470, 'ravi': 2546465467}
print('1.single contact search')
print('2.display all the contacts')
print('3.display multipal contact number')
ac = (int(input('what do you wanna do? ')))

if ac == 1:
    ts = str(input('whom number you want:'))
    if ts in cl:
        print(cl[ts])
    else:
        print('please only enter the name of person which are in our class')
elif ac == 2:
    print(cl.items())
elif ac == 3:
    np = int(input('how many people contact number you want:'))
    for i in range(np):
        pe = str(input('enter the name:'))
        print(cl[pe])