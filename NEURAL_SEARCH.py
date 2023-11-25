#Importing.....
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from MMR import get_results
from openai import OpenAI
import os 
client = OpenAI()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
# OPENAI API KEY
# PLEASE Replace with your API KEY
os.environ['OPENAI_API_KEY']="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"



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

'''
Neural Searcher class. 
This class is responsible for fetching results from vector database which are similar to user query and displaying the results.

'''

class NeuralSearcher:
    def __init__(self, collection_name:str):
        '''
        collection_name: Name of the Qdrant Collection

        '''
        self.collection_name = collection_name 
        # Initialize encoder model
        self.model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
        # initialize Qdrant client
        self.qdrant_client = QdrantClient("http://localhost:6333")

    def search(self, text: str):
        '''
        Inputs: 
            text: user query(string)
        Outputs:
            responses: ChatGPT (LLM) summary
            payloads : JSON format data from vector database
        '''
        # Convert text query into vector
        vector = self.model.encode(text).tolist()

        # Retrieving 20 most similar vectors to user query

        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=None,  
            limit=20 
        )
    
        indices=[hit.id for hit in search_result] # Extracting indices from the results fetched so far
        indices=get_results(indices,vector)# Using MMR Algorithm to sort the results based on decreasing order of MMR Score
        selected_indices=indices[:5]#Taking only top 5 vectors for final results.Use of MMR ensures diverse results.
        payloads = [hit.payload for hit in search_result if hit.id in selected_indices]
        summary=[]
        # Generating summary from CHAT GPT (LLM)
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You would be given the results of a search query by user on a database. Describe the results like a marketer with numerical details in a paragraph style manner."},
            {"role": "user", "content": text},
            {"role": "user", "content": str(payloads)}
        ]
        )
        response=response.choices[0].message.content
        return response,payloads # function return 
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    

