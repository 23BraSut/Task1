# Semantic Similarity with spaCy
This code demonstrates how to use spaCy's en_core_web_md model to calculate semantic similarity between words and sentences.

### Installation
To run this code, you will need to have 
- Python 3
- spaCy installed:

pip install spacy
- You will also need to download the en_core_web_md model by running:

python -m spacy download en_core_web_md
Running the code
- Once you have installed the necessary dependencies
- you can run the semantic.py file in a Python environment.

### python semantic.py
- The script will output similarity scores between words and sentences. 
- You can modify the script to calculate similarity scores between your own words and sentences.

### Docker
Alternatively, you can run the code using Docker. 
- To do so, you will first need to build the Docker image:
- docker build -t semantic-similarity .
- After building the image, you can run the code in a Docker container:
- docker run semantic-similarity

Pulling from Docker
- To pull the Docker image from Docker Hub, you can run:
- docker pull 23brasut/semantic-similarity
- Then docker run 23brasut/semantic-similarity

### Sample Output
- The output of the script will look like this:
0.5015
0.2433
0.2593
0.8961
0.8375
0.7586
cat cat 1.0
cat apple 0.338
cat monkey 0.502
cat banana 0.243
apple cat 0.338
apple apple 1.0
apple monkey 0.394
