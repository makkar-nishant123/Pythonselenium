
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

   if len(result)<=0:
       for k, v in sorted(output.items(),reverse=True):
               if (v < max):
                 result.append(list(k))
                 break

   print(result)




optimalUtilization(20,[[1,8],[2,7],[3,14]],[[1,5],[2,10],[3,14]])