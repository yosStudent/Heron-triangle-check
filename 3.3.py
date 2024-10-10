import math

area=0

def input_float(number_for_transforming):
    while True:
        try:
            user_input=input(number_for_transforming)
            user_input = user_input.replace(',','.')
            user_input=float(user_input)
            return user_input
        except ValueError:
            print("Wrong format of provided data, try again")

def triangle_possibility_check(a,b,c):
    if a+b<c and a+c<b and b+c<a:
        result = False
    else:
        result = True
    return result

def is_triangle_Pigor(a,b,c):
    if triangle_possibility_check(a,b,c) is True:
        if c**2- a**2 - b**2==0 or a**2-c**2-b**2==0 or b**2-c**2-a**2==0:
            Thisisit=True
        else:
            Thisisit=False
    else:
        Thisisit=False
    return Thisisit

def Heron_formule(a,b,c):
    if triangle_possibility_check(a,b,c) is True:
        halfrimetr=(a+b+c)/2
        area = math.sqrt(halfrimetr*((halfrimetr-a)*(halfrimetr-b)*(halfrimetr-c)))
        return area
    else:
        print("Unreal triangle")

a=input_float('Provide 3 sides of triangle:\nFirst: ')
b=input_float('Second: ')
c=input_float('Third: ')

if triangle_possibility_check(a, b, c) is True:
    print('This triangle can be')
    print(f'Perimetr of this triangle according to Heron formula is {Heron_formule(a,b,c)}')
else:
    print("This triangle can't be")
'''
Optional part with * task

# List triangles:
triangles = [
    (3, 4, 5),   # First triangle with sides 3, 4 и 5
    (5, 12, 13), # Second triangle with sides 5, 12 и 13
    (8, 15, 17)  # And the third one
]

# Combinations:
for triangle_sides in triangles:
    a, b, c = triangle_sides
    area = area_of_triangle(a, b, c)
    print(f'Area of triangle with sides {a}, {b}, {c} is equal {Heron_formule(a,b,c)}')
'''