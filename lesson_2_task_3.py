import math

def square(side):
    area = side * side
    return math.ceil(area) if side != int(side) else area

# Тестирование
print(f"Площадь квадрата со стороной 5: {square(5)}")        
print(f"Площадь квадрата со стороной 3.2: {square(3.2)}")    
print(f"Площадь квадрата со стороной 2.7: {square(2.7)}") 