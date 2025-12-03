cities = ["Москва", "Санкт-Петербург", "Казань", "Екатеринбург"]
l = cities[:]
print(id(cities)== id(l))

print(cities[1:3])
print(cities[3:])
print(cities[0:3])
print(cities[:])
print(cities[-2:])

print(cities[::2])
print(cities[::-1])
print(cities[::-2])

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

print(["Python", "rocks"] *2)

print(a == [1, 2, 3])
print([10, 5, 3] > [5, 10, 3])
print([1, 2, 3] > [1, 2, 2])

chars = list("Python")
print(chars)
print(max(chars))
print(min(chars))
