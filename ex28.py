# In this exercise you will take the logic exercises you memorized and start trying them in Python.
# Take each of these logic problems and write down what you think the answer will be.
# In each case it will be either True or False.
# Once you have the answers written down,
# start Python in your Terminal and type each logic problem in to confirm the answer

True and True

False and True

1 == 1 and 2 == 1

"test" == "test"

1 == 1 or 2 != 1

True and 1 == 1

False and 0 != 0

True or 1 == 1

"test" == "testing"

1 != 0 and 2 == 1

"test" != "testing"

"test" == 1

not (True and False)

not (1 == 1 and 0 != 1)

not (10 == 1 or 1000 == 1000)

not (1 != 10 or 3 == 4)

not ("testing" == "testing" and "Zed" == "Cool Guy")

1 == 1 and (not ("testing" == 1 or 1 == 0))

"chunky" == "bacon" and (not (3 == 4 or 3 == 3))

3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

# I will also give you a trick to help you figure out the more complicated ones toward the end.
# Whenever you see these Boolean logic statements, you can solve them easily by this simple process.

# 1. Find an equality test (== or !=) and replace it with its truth.
# 2. Find each and/or inside parentheses and solve those first.
# 3. Find each not and invert it.
# 4. Find any remaining and/or and solve it.
# 5. When you are done you should have True or False.


###
# Isn't there a shortcut?
# Yes.
# Any and expression that has a False in immediately False, so you can stop there.
# Any or expression that has a True is immediately True, so you can stop there.
# But make sure you can process the whole expression because later it becomes helpful.
###
