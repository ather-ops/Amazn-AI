from src.data_loader import load_dataset
from src.chunking import create_chunks

df = load_dataset()

chunks, metadata, ids = create_chunks(df)

print(f"Total Chunks : {len(chunks)}")
print(f"Total Metadata : {len(metadata)}")
print(f"Total IDs : {len(ids)}")

print("\nFirst Chunk\n")
print(chunks[0])

print("\nFirst Metadata\n")
print(metadata[0])

print("\nFirst ID\n")
print(ids[0])