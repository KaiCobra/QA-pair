from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertModel.from_pretrained('bert-base-chinese')

def get_message_embedding(message):
    # Split the message into chunks if it's too long
    max_length = 512
    inputs = tokenizer(message, return_tensors="pt", truncation=True, max_length=max_length)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def f(x):
    return 1 / (1 + np.exp(-x))

def compute_similarity_matrix(messages):
    # Get embeddings for each message
    embeddings = [get_message_embedding(message) for message in messages]
    embeddings = np.array(embeddings)
    
    # Compute cosine similarity matrix
    cosine_sim_matrix = cosine_similarity(embeddings)
    
    # Adjust similarity matrix with time difference weights
    num_messages = len(messages)
    time_weight_matrix = np.ones((num_messages, num_messages))
    
    # For simplicity, assume messages are equally spaced in time
    for i in range(num_messages):
        for j in range(num_messages):
            time_diff = -(i - j)
            if time_diff>=0:
                # Calculate the combined result for x >= 0
                time_weight_matrix[i, j] = f(time_diff)*(np.sqrt(1 / (1 + time_diff)))
            else:
                # Calculate the combined result for x < 0
                time_weight_matrix[i, j] = f(time_diff)*(1 / (1 + np.abs(time_diff)))**2
                
    
    # Combine cosine similarity and time weight matrices
    final_similarity_matrix = cosine_sim_matrix * time_weight_matrix
    
    return final_similarity_matrix

def find_most_similar_pairs(similarity_matrix, messages):
    num_messages = len(messages)
    pairs = []
    
    for i in range(num_messages):
        most_similar_index = np.argsort(similarity_matrix[i, :])[-2]  # -1 would be the message itself
        pairs.append({
            "question": messages[i],
            "answer": messages[most_similar_index],
            "similarity": similarity_matrix[i, most_similar_index]
        })
    
    return pairs
