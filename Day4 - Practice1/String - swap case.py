value = str(input())

# for data in value:
#
#     if data.isupper():
#         print (data.lower() , end = '')
#
#     elif data.islower():
#         print (data.upper() , end = '')
#
#     else:
#         print (data , end = '')


def upperlower(string):
    upper = 0
    lower = 0

    for i in range(len(string)):

        # For lower letters
        if (ord(string[i]) >= 97 and
                ord(string[i]) <= 122):
            print (string[i] , end = '')

        # For upper letters
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90):
            print (string[i] , end = '')

        else:
            print (string[i] , end = '')

    #print('Lower case characters = %s' % lower,
     #     'Upper case characters = %s' % upper)

upperlower(value)
