# ranges using range method
# ranges are immutable types

# range(start, stop, step)
range(0, 5, 1)

print(list(range(0, 5, 1)))

print(list(range(2, 13, 2)))

x = 1
print(list(range(2, 13, x + 1)))

# if the step value is positive
#
# r[i] = start + (step * i)
#
# where i >= 0 and r[i] < stop

print(list(range(3, -8, -2)))

print(list(range(6)))

range1 = range(0, 10, 6)
range2 = range(0, 11, 6)

print("range 1:", list(range1))
print("range 2:", list(range2))

if range1 == range2:
    print("range 1 = range 2")

mylist = [2, 4, 6, 8, 10]
my_range = range(2, 10, 2)

print("myrange.start", my_range.start)
print("myrange.stop", my_range.stop)
print("myrange.step", my_range.step)

print("Run a loop body 10x")

for i in range(10):
    print(i)

print("Counter from 3 to 20 by step 5")

for i in range(3, 20, 5):
    print(i)

# no concatenation or repetition

if 1 in range(0, 4):
    print("1 is in the range")

if 10 not in range(0, 4):
    print("10 in not in the range")

print("len:", len(range(0, 4)))
print("min:", min(range(0, 4)))
print("max:", max(range(0, 4)))

print(range(0, 10).count(1))

print(range(2, 6).index(4))

print(range(2, 6)[1])

print(list(range(0, 20, 2)[2:10:3]))
