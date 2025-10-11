import numpy as np

rng = np.random.default_rng()

## Random Number
print(rng.integers(low=1, high=7, size=3))
print(np.random.uniform(low=-1, high=1, size=(3, 2)))


## shuffle()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)


## choice()
fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🥭"])
fruits = rng.choice(fruits,size=(3, 3))
print(fruits)




# Exercise
# 2D array of Emojis

emojis = np.array(["😊", "😂", "😎", "😉", "🤑"])
emojis = rng.choice(emojis, size=(3, 3))
print(emojis)