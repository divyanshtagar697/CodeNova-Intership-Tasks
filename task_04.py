import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = {
    'Income': [15, 16, 17, 18, 19, 70, 72, 75, 78, 80, 20, 21, 85, 90, 95],
    'Spending': [39, 81, 6, 77, 40, 50, 48, 55, 60, 45, 10, 15, 90, 85, 98]
}
df = pd.DataFrame(data)
kmeans = KMeans(n_clusters=3, n_init=10)
df['Segment'] = kmeans.fit_predict(df[['Income', 'Spending']])
plt.scatter(df['Income'], df['Spending'], c=df['Segment'], cmap='rainbow')
plt.title('Customer Segments')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

print("Clusters Created:")
print(df)
