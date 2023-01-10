# birthday-paradox
Testing (and proving) the [Birthday Paradox](https://en.wikipedia.org/wiki/Birthday_problem) with Python

I heard about the [Birthday Paradox](https://en.wikipedia.org/wiki/Birthday_problem) on a podcast and was intrigued enough to write this little Python script. The paradox is that with as few as 23 random people in a group, there's a 50% chance that 2 of them will share a birthday. 

This code uses a randomly generated list (birthday_list.txt) of 1000 first names, each with a randomly assigned birthday. And then the script tests the paradox by grabbing a predefined number of people from the list, and checking to see how many of them share a birthday. As expected, the paradox is proven true. In fact, with as few as 45 people you will find upwards of 98% probability that at least 2 of them will share a birthday!

When the script (birthdayCollision.py) is ran, it prints out a sentence like this:  
"For 1000 groups of 23 random people each, at least 2 people's birthdays matched 485 times, which is 52%"

Mostly self explanatory, but it grabbed x random names (and their birthdays) from birthday_list.txt, found how many "collisions" (shared birthdays) are in the group, and then reports the results. It does this x times (1000 in this case) to get a percentage of how many times the paradox was true, I.E., how many times at least 2 birthdays were shared among the people in each of the 1000 groups. And in this case that percentage was 52%. Running the script multiple times will yield slightly different percentages. Also, you can modify the num_iterations and group_size variables to play with different numbers and see the results.
