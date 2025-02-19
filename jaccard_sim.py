import pandas as pd
import numpy as np
def jaccard_similarity(sent1, sent2):
    
    words1 = set(sent1.lower().split())
    words2 = set(sent2.lower().split())
    
    
    intersection = words1 & words2  
    union = words1 | words2  
    
    similarity = len(intersection) / len(union)
    return similarity*100


sentences = [
    "The stock market is experiencing a significant rise in prices today.",
    "Stock prices are increasing today due to strong market trends.",
    "The economy is growing as stock prices continue to rise.",
    "The stock market is experiencing a significant rise in prices today.",
    "Investors are closely watching market trends as stock prices fluctuate.",
    "Stock market volatility increases when global economic conditions are uncertain.",
    "Strong corporate earnings reports have pushed stock prices to new highs."
]


m = len(sentences)
jaccard_matrix = np.zeros((m, m))

for i in range(m):
    for j in range(m):
            jaccard_matrix[i][j] = jaccard_similarity(sentences[i], sentences[j])


df = pd.DataFrame(jaccard_matrix, index=sentences)
print(df)