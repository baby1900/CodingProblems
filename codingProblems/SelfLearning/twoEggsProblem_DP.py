'''
Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from,
 and which will cause the eggs to break on landing. We make a few assumptions:

…..An egg that survives a fall can be used again.
…..A broken egg must be discarded.
…..The effect of a fall is the same for all eggs.
…..If an egg breaks when dropped, then it would break if dropped from a higher floor.
…..If an egg survives a fall then it would survive a shorter fall.
…..It is not ruled out that the first-floor windows break eggs,
 nor is it ruled out that the 36th-floor do not cause an egg to break.

If only one egg is available and we wish to be sure of obtaining the right result,
the experiment can be carried out in only one way. Drop the egg from the first-floor window;
if it survives, drop it from the second floor window. Continue upward until it breaks.
In the worst case, this method may require 36 droppings. Suppose 2 eggs are available.
What is the least number of egg-droppings that is guaranteed to work in all cases?

The problem is not actually to find the critical floor,
 but merely to decide floors from which eggs should be dropped so that total number of trials are minimized.

'''



def twoEggsProblem(floorNum, eggNum):
    dp = [[0 for i in range(eggNum + 1)] for j in range(floorNum + 1)]
    for k in range(2):
        for i in range(eggNum + 1):
            dp[0][i] = k
    for j in range(floorNum + 1):
        dp[j][0] = 0
        dp[j][1] = j
    for floor in range(2, floorNum + 1):
        for egg in range(2, eggNum + 1):
            dp[floor][egg] = floorNum
            for currfloor in range(1, floor + 1):
                currans = max(dp[currfloor - 1][egg - 1], dp[floor - currfloor][egg]) + 1
                if currans < dp[floor][egg]:
                    dp[floor][egg] = currans
    return dp[floorNum][eggNum]


assert(twoEggsProblem(100,2)) == 14
