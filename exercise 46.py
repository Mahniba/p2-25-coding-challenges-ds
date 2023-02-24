def max_number(array):
    if len(array)==1:
        return array[0]
    point =len(array) // 2
    m1 = max_number(array[:point])
    m2 = max_number(array[point:])
    if m1>m2:
        print(f"m1 ={m1} larger > m2 {m2}")
        return m1
    else:
        print(f"m2 = {m2} larger > m1 {m1}")
        return m2


print(max_number([1,3,5,7]))