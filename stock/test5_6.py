def get_triangle_area(width , height) :
    return (width * height) / 2
print(get_triangle_area(10,5))

def add_start_to_end(start , end) :
   return sum(range(start , end))
print(add_start_to_end(0 , 10+1))

def get_str(text) :
    a = []
    for i in text :
        a.append(i[:3])
    return a
print(get_str(["Seoul", "Daegu", "Kwangju", "Jeju"]))