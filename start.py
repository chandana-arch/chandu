input=int(input('enter val'))
if input%2==0:
    print('even',input)
else:
    print('odd',input)
def palin(input):
    return input[::-1]==input