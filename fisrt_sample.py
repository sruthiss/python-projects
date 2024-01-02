# this is the sample python function printout
def fucntion_loop_testing( var_list,list2 ):
    newlist=zip(var_list,list2)
    for k in newlist:
        print(k)
    return newlist

list_name=['sruthi','ThayalaVishnu','Praveen']
age_lsit=[29,3,34]
ziped_lsit=fucntion_loop_testing(list_name,age_lsit)
print(ziped_lsit)