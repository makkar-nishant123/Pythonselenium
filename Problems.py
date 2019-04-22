
def optimalUtilization(max,listdata1,listdata2):
   output_dictionary = dict()
   output_dictionary2 = dict()
   output = dict()
   result = list()
   for data in listdata1:

        output_dictionary[data[0]] =data[1]
   for data in listdata2:
       output_dictionary2[data[0]] = data[1]


   for k1, v1 in output_dictionary.items():
        for k2 , v2 in output_dictionary2.items():

            output[(k1,k2)] = str(v1+v2)
   for k , v in sorted(output.items()):
       if str(v) == str(max):
            result.append(list(k))
       print (res)




optimalUtilization(10000,[[1,3000],[2,5000],[3,7000],[4,10000]],[[1,2000],[2,3000],[3,4000],[4,5000]])