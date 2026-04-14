print("Movie Rating")

movies = ["A", "B", "C"]
ratings = []

for i in range(3):
    rate = float(input("Enter rating: "))
    ratings.append(rate)

avg = sum(ratings) / 3

if avg > 4:
    print("Excellent")
else:
    print("Average")

print("Average Rating:", avg)

for i in range(2):
    print("Done")

print("End")
