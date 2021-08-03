
a1=[2,4,5,9]
a2=[1,4,3,2]
def elt_in_arr1(a1,a2):
        return [x for x in a1 if x not in a2]
print(elt_in_arr1(a1,a2))

