# Write your code here :-)
import turtle as t

for i in range(4):
    t.forward(200)
    t.right(90)

print("Hello on a snowy day!")

dog = ("Finn", "fat", 8)
cat = ["Skipper", "fast",6]
bird = [dog, cat]
bird[1][1]= 54
cat[2] = "slow"
dog[2] = "cheesey"
print(bird)