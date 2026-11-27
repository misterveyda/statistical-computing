import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Select numerical variables
X = patients[['Age', 'WaitingMinutes', 'VisitsPerYear']]

# Handle missing values
X = X.dropna()

# Standardize the variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA()
principal_components = pca.fit_transform(X_scaled)

# Display explained variance
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Display principal component loadings
loadings = pd.DataFrame(
    pca.components_.T,
    index=X.columns,
    columns=['PC1', 'PC2', 'PC3']
)

print("Principal Component Loadings:")
print(loadings)
