import numpy as np
from sklearn.neighbors import NearestNeighbors


def main():
    features = np.load("merged_features.npy_01.npy")
    nn = NearestNeighbors(
        n_neighbors=20,
        algorithm='brute',
        metric='euclidean'
    ).fit(features)
    distances, indices = nn.kneighbors(features[0], n_neighbors=20)
    return features[indices.flatten()]


if __name__ == "__main__":
    main()
