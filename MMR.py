

import numpy as np
import math
from sklearn.metrics.pairwise import cosine_similarity


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def euclidean_similarity_matrix(data):
    """
    Compute the similarity matrix using Euclidean similarity for a dataset.

    Parameters:
        - data (numpy array): A 2D numpy array where each row represents a sample and each column represents a feature.

    Returns:
        - similarity_matrix (numpy array): A square matrix containing the similarity scores between features.
    """
    transposed_data = np.transpose(data)
    num_features = transposed_data.shape[0]
    similarity_matrix = np.zeros((num_features, num_features))

    for i in range(num_features):
        for j in range(num_features):
            # Calculate the Euclidean distance between feature vectors i and j
            euclidean_distance = np.linalg.norm(transposed_data[i] - transposed_data[j])
            # Convert distance to similarity score (use 1/distance to represent similarity)
            similarity_matrix[i, j] = 1.0 / (1.0 + euclidean_distance)
    return similarity_matrix
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def MMR(relevance_scores,similarity_matrix,alpha):

    """
    Maximum Marginal Relevance (MMR) feature selection using Euclidean similarity.

    Parameters:
            - relevance_scores (array-like): Relevance scores of features with respect to the target variable.
            - similarity_matrix (array-like): Matrix containing similarity scores between features.
            - alpha (float): Trade-off parameter between relevance and redundancy (0 <= alpha <= 1).

    Returns:
        - selected_indices (list): List of indices of the selected features.
    """
    num_features = len(relevance_scores)
    selected_indices = []
    remaining_indices = list(range(num_features))

    while len(selected_indices) < num_features:
        max_mmr_score = -float('inf')
        best_index = None

        for idx in remaining_indices:
            # Calculate MMR score for each feature
            relevance_score = relevance_scores[idx]
            if len(selected_indices) > 0:
                similarity_with_selected = np.mean(similarity_matrix[idx, selected_indices])
            else:
                similarity_with_selected = 0.0  # No similarity if no features are selected
            mmr_score = alpha * relevance_score - (1 - alpha) * similarity_with_selected

            if mmr_score > max_mmr_score:
                max_mmr_score = mmr_score
                best_index = idx

        selected_indices.append(best_index)
        remaining_indices.remove(best_index)
    

    return selected_indices
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def get_results(indices,query_vec):
    vectors=np.load('vectors.npy')
    vectors_dict={}

    for key in range(len(indices)):
        vectors_dict[key]=indices[key]

    query_vec=np.array(query_vec).reshape(1,-1)
    vectors=vectors[indices]
    sim_matrix=euclidean_similarity_matrix(vectors)
    # Calculate the information gain for each feature with respect to the target variable
    feature_importance = cosine_similarity(vectors,query_vec)
    selected_features = MMR(relevance_scores=feature_importance, similarity_matrix=sim_matrix, alpha=0.5)
    selected_features=[vectors_dict[key] for key in selected_features]

    return selected_features

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#