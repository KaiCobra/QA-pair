from flask import Flask, request, jsonify, render_template
from _matrix import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
from matplotlib import font_manager
import matplotlib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/similarity', methods=['POST'])
def similarity():
    data = request.json
    messages = data['messages']
    
    # Compute similarity matrix
    similarity_matrix = compute_similarity_matrix(messages)
    
    # Find most similar pairs
    pairs = find_most_similar_pairs(similarity_matrix, messages)
    num_msg = len(messages)
    # Get message labels (first 7 characters)
    labels = [message[:7] for message in messages]
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    matplotlib.rcParams.update({'font.size': 1.1*num_msg})
    
    # Plot similarity matrix
    plt.figure(figsize=(num_msg*2,num_msg*2))
    sns.heatmap(similarity_matrix, annot=True, cmap='coolwarm', xticklabels=labels, yticklabels=labels,fmt = '.2f')
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    
    # Save plot to a string in base64 format
    img = io.BytesIO()
    plt.savefig(img, format='png',bbox_inches = 'tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return jsonify({'plot_url': plot_url, 'pairs': pairs})

if __name__ == '__main__':
    app.run(debug=True)
