# # Install these libraries
# !pip install qdrant-client --user
# !pip install faker
# !pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# !pip install sentence_transformers
# !pip install fastapi uvicorn

import pandas as pd 
import numpy as np
import os 
import numpy as np
import json
from sentence_transformers import SentenceTransformer
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance


#----------------------------------------------------------------------------------------------------------------------------------------#
collection_name="Promit_BIGBasket_CHAABI"
path_data=r'bigb.csv'
name_model="all-MiniLM-L6-v2"
device="cuda"
#----------------------------------------------------------------------------------------------------------------------------------------#

" Importing necessary modules"

print("Loading encoding model......")
# Encoding model
model = SentenceTransformer(name_model,device=device)
print("Encoding model loaded.... {}".format(name_model))
num_size=dim_size=model.get_sentence_embedding_dimension()

#Converting csv data to a dictionary 

data=pd.read_csv(path_data)

docs=[]
columns=data.columns
for idx in range((data.shape[0])):
    record={
        "index":data['index'][idx],
        "product":data['product'][idx],
        "category":data['category'][idx],
        "sub_category":data['sub_category'][idx],
        "brand":data['brand'][idx],
        "sale_price":data['sale_price'][idx],
        "market_price":data['market_price'][idx],
        "type":data['type'][idx],
        "rating":data['rating'][idx],
        "description":data['description'][idx]
    }
    docs.append(record)
    print("Completed :{}/{}".format(idx+1,data.shape[0]),end="\r")

print("Data converted into dictionary format .....")
#----------------------------------------------------------------------------------------------------------------------------------------#

# Converting dataframe to json 

data.to_json('file.json',orient='records',compression='infer')


fd=open("file.json")
payload=json.load(fd)
df = pd.read_json("file.json", lines=True)

new_list=list(df[df.columns])
temp_list=list([str(df[col][0]) for col in df.columns])

vectors=model.encode(temp_list)
np.save("vectors.npy", vectors, allow_pickle=False)
#----------------------------------------------------------------------------------------------------------------------------------------#

qdrant_client = QdrantClient("http://localhost:6333")
qdrant_client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)

print("Pleas wait while we are uploading the data to a vector database.........")

qdrant_client.upload_collection(
    collection_name=collection_name,
    vectors=vectors,
    payload=payload,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256,  # How many vectors will be uploaded in a single request?
)

print(" Vector Database Created Successfully!!")
#----------------------------------------------------------------------------------------------------------------------------------------#
