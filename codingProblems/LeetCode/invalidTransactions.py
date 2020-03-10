'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes),
amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes,
have the same name and is in a different city. Similarly the second one is invalid too.
'''
import operator
def invalidTransactions(transactions):
    outset = set()
    sortedTransactions = []
    for transaction in transactions:
        name, time, amount, city = transaction.split(',')
        sortedTransactions.append([name, int(time), int(amount), city, transaction])

    sortedTransactions = sorted(sortedTransactions, key=operator.itemgetter(0, 1))
    for i in range(len(sortedTransactions)):
        transaction = sortedTransactions[i]
        if transaction[2] > 1000:
            outset.add(transaction[4])
        j = i + 1
        while j < len(sortedTransactions) and transaction[0] == sortedTransactions[j][0] and transaction[1] + 60 >= sortedTransactions[j][1]:
            if transaction[3] != sortedTransactions[j][3]:
                outset.add(sortedTransactions[j][4])
                outset.add(transaction[4])
            j += 1

    return list(outset)