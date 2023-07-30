from apriori import Apriori

if __name__ == '__main__':
    filePath = 'DBMS/Apriori/data/retail_dataset.csv'
    minSup = 0.2
    # minSup = float(input('Enter Min Support: '))
    minConf = 0.4

    obj = Apriori(minSup, minConf)
    itemCountDict, freqSet = obj.fit(filePath)
    for key, value in freqSet.items():
        print('Frequent {}-term set: '.format(key))
        print('-'*20)
        for itemset in value:
            print(list(itemset))

        print()

    rhs = frozenset([input("Item: ")])
    rules = obj.getSpecRules(rhs)
    print('-'*20)
    print('rules refer to {}'.format(list(rhs)))
    for key, value in rules.items():
        print('{} -> {}: {}'.format(list(key), list(rhs), value))