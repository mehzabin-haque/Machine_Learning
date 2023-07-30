from itertools import combinations

                
def getItemList(transactions):
    unique_items = []
    for transaction in transactions:
        for item in transaction[1]:
            if item not in unique_items:
                unique_items.append(item);
    unique_items.sort()
    return unique_items

def pruneBasedOnSubset(ci,transactions):
    temp = ci.copy()
    all_itemset = [item[1] for item in transactions]


    for candidate in temp.keys():
        for subset in combinations(candidate, len(list(temp.keys())[0])-1):
            if list(subset) not in all_itemset:
                if len(list(temp.keys())[0])-1 != 1:
                    #print(list(subset), all_itemset)
                    del ci[candidate]
                    break
    return ci


def apriori(transactions, support_vector):
    unique_items = getItemList(transactions)

    C1 = {}
    for item in unique_items:
        for transaction in transactions:
            if item in transaction[1]:
                if item in C1.keys():
                    C1[item]+=1
                else: C1[item] = 1
    print("Set of Candidate 1-itemset, C1: \n"+str(C1)+"\n")

    # Set of frequent 1-itemset = L1
    L1 = {}
    for item,count in zip(C1.keys(), C1.values()):
        if count>=support_vector:
            if item in L1: L1[frozenset([item])]+=count
            else: L1[frozenset([item])] = count
    print("Set of frequen 1-itemset, L1: \n"+str(L1)+"\n")

    # Now, we will do the above for itemset 2..n
    Li = {} # Set of frequent i-itemset
    Ci = {} # Set of Candidatge i-itemset

    Li = L1 # Initializing
    Ci = C1

    total_result = []
    for item_size in range(2,1000):
        # Candidate itemset, Ci
        # Join
        new_items = joinItems(Li, item_size)
        print("After Join: \n"+str(new_items)+"\n")

        # Count
        Ci = {}
        for item in new_items:
            Ci[item] = 0
            for transaction in transactions:
                temp = set(transaction[1])
                if(item.issubset(temp)):
                    Ci[item]+=1
        print("Candidate Set. C"+str(item_size)+":\n"+str(Ci)+"\n")

        # Ci = pruneBasedOnSubset(Ci, transactions)

        # Frequent Itemset, Li
        # Pruning
        Li = {}
        for item in Ci:
            if Ci[item] >= support_vector:
                Li[item] = Ci[item]
        print("Accepted itemset, L"+str(item_size)+":\n"+str(Li)+"\n")

        total_result.append(Li)
        if(len(Li)==0): return total_result

def joinItems(Li, item_size):
    old_items = [item for item in Li.keys()]
    new_items = []
    for i in range(0, len(old_items)):
        for j in range(i+1, len(old_items)):
            new_item = old_items[i].union(old_items[j])
            if(len(new_item)==item_size):
                new_items.append(new_item)

    new_items.sort()
    return new_items

# Testing

transactions = [
["TID1" ,      ["MILK","BREAD","BISCUIT"]],
["TID2" ,  ["BREAD","MILK","BISCUIT","CORNFLAKES"]],
["TID3" ,  ["BREAD","TEA","BOURNVITA"]],
["TID4" ,  ["JAM","MAGGI","BREAD","MILK"]],
["TID5" ,  ["MAGGI","TEA","BISCUIT"]],
["TID6" ,  ["BREAD","TEA","BOURNVITA"]],
["TID7" ,  ["MAGGI","TEA","CORNFLAKES"]],
["TID8" ,  ["MAGGI","BREAD","TEA","BISCUIT"]],
["TID9" ,  ["JAM","MAGGI","BREAD","TEA"]],
["TID10",   ["BREAD","MILK"]],
["TID11",   ["COFFEE","COCK","BISCUIT","CORNFLAKES"]],
["TID12",   ["COFFEE","COCK","BISCUIT","CORNFLAKES"]],
["TID13",   ["COFFEE","SUGER","BOURNVITA"]],
["TID14",   ["BREAD","COFFEE","COCK"]],
["TID15",   ["BREAD","SUGER","BISCUIT"]],
["TID16",   ["COFFEE","SUGER","CORNFLAKES"]],
["TID17",   ["BREAD","SUGER","BOURNVITA"]],
["TID18",   ["BREAD","COFFEE","SUGER"]],
["TID19",   ["BREAD","COFFEE","SUGER"]],
["TID20",   ["TEA","MILK","COFFEE","CORNFLAKES"]]
]

print("Final Answer:\n"+str(apriori(transactions, support_vector=2)))