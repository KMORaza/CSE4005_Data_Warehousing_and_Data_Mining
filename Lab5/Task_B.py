import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
transactions = [
    ["a", "b", "c"],
    ["a", "b"],
    ["a", "b", "d"],
    ["b", "e"],
    ["b", "c", "e"],
    ["a", "d", "e"],
    ["a", "c"],
    ["a", "b", "d"],
    ["c", "e"],
    ["a", "b", "d", "e"],
    ["a", "b", "e", "c"]
]
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=3/len(df), use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
print(rules)

