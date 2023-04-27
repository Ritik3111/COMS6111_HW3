
import pandas as pd
import itertools
import sys

def apriori(dataset, min_supp):
    # Step 1: Convert dataset to a list of transactions
    transactions = []
    for row in dataset:
        transactions.append(set(row))

    # Step 2: Create a dictionary of items and their frequency
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
    
    # Step 3: Remove items that do not meet the minimum support threshold
    items = set(item_counts.keys())
    for item in items:
        if item_counts[item] / len(transactions) < min_supp:
            del item_counts[item]

    items = set(item_counts.keys())
    # Step 4: Generate frequent itemsets of length 1
    frequent_itemsets = []
    for item in item_counts:
        support = item_counts[item] / len(transactions)
        if support >= min_supp:
            frequent_itemsets.append(frozenset([item]))

    Freq_Sets = dict()
    Freq_Sets[1] = frequent_itemsets
    # Step 5: Generate frequent itemsets of length 2 and higher
    k = 2
    while k<len(transaction):
        print(k)
        candidate_itemsets = []
        candidate_itemsets = [subset for subset in list(itertools.combinations(items, k))]
        candidate_itemsets = set(candidate_itemsets)
        #print(candidate_itemsets)
        frequent_itemsets = []
        for candidate_itemset in candidate_itemsets:
            candidate_itemset = frozenset(candidate_itemset)
            count = 0
            for transaction in transactions:
                if candidate_itemset.issubset(transaction):
                    count += 1
            support = count / len(transactions)
            if support >= min_supp:
                frequent_itemsets.append(candidate_itemset)
                item_counts[candidate_itemset] = count
        #print(frequent_itemsets)
        if len(frequent_itemsets) == 0:
            break
        Freq_Sets[k] = frequent_itemsets
        #print(Freq_Sets[k])
        k += 1

    # Return frequent itemsets and association rules
    return Freq_Sets,item_counts,transaction

def get_rules(frequent_itemsets,item_counts,transactions,min_supp,min_conf):
    rules = []
    for key,itemsets in frequent_itemsets.items():
        for itemset in itemsets:
            for consequent in itemset:
                consequent = {consequent}
                antecedent = itemset - consequent
                if len(antecedent) >= 1 and len(consequent) == 1:
                    consequent = list(itemset - antecedent)[0]
                    if consequent not in antecedent:
                        itemset_count = item_counts[itemset]
                        if len(antecedent) == 1:
                            antecedent_count = item_counts[list(antecedent)[0]]
                        else:
                            antecedent_count = item_counts[antecedent]
                        support = itemset_count / len(transactions)
                        confidence = itemset_count / antecedent_count
                        if confidence >= min_conf and support >= min_supp:
                            #print((antecedent, frozenset([right_side_item]), support, confidence))
                            rules.append((antecedent, frozenset([consequent]), support, confidence))
    return rules

def main():
    dataFile = pd.read_csv(sys.argv[1])
    dataset = dataFile.values
    minSupp = float(sys.argv[2])
    minConf = float(sys.argv[3])
    frequent_itemsets,item_counts,transactions = apriori(dataset, minSupp)
    rules = get_rules(frequent_itemsets,item_counts,transactions,minSupp,minConf)
    sorted_rules = set(sorted(rules, key=lambda x: x[3], reverse= True))

    with open('output.txt', 'w') as file:
        for ilist in frequent_itemsets.values():
            for item in ilist:
                item = list(set(item))
                if len(item) == 1:
                    support = item_counts[item] / len(transactions)
                else:
                    support = item_counts[item] / len(transactions)
                file.write("%s , %.2f%%" % (str(item), support*100))

    with open('output.txt', 'w') as file:
        for item in sorted_rules:
            file.write(item[0]+ ' ==> ' + item[1] + " (Conf: %.2f%% " % (item[3]*100) + ", Supp: %.2f%%)" % (item[4]*100))
        
if __name__ == '__main__':
    main()

