import numpy as np
from sklearn.neighbors import NearestNeighbors

features = np.load("merged_features.npy_01.npy")
# Make the features array longer
features = np.vstack([features] * 10)

def main():
    nn = NearestNeighbors(
        n_neighbors=20,
        algorithm='brute',
        metric='euclidean'
    ).fit(features)
    distances, indices = nn.kneighbors(features[0], n_neighbors=20)
    return features[indices.flatten()]


if __name__ == "__main__":
    main()
