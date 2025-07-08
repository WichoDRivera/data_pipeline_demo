from functions import *
import time
import datetime

print("Starting data pipeline at ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("-----------------------------------------------")

# Step 1: extract video IDs
t0 = time.time()
getVideoIDs()
t1 = time.time()
print("Step 1: Done")
print("---> Video IDs downloaded in", str(t1-t0), " seconds", "\n")

# Step 2: Extract transcripts for videos
t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print("Step 2: Done")
print("---> Transcripts downloaded in", str(t1-t0), " seconds", "\n")

# Step 3: Transform data
t0 = time.time()
transformData()
t1 = time.time()
print("Step 3: Done")
print("---> Data transformed in", str(t1-t0), " seconds", "\n")

# Step 4: Generate text embeddings
# Info: Embeddings are a numerical representation of the essential information of a video in a fixed-lenght vector
t0 = time.time()
createTextEmbeddings()
t1 = time.time()
print("Step 4: Done")
print("---> Embeddigns generated in", str(t1-t0), " seconds", "\n")