# Distributing Workload Evenly in Chunks

from mod.multiprocess_queue import chunk_indices

print("\n\n\n" + ("="*60) + "\n\n\tDistributing Workload Evenly in Chunks\n\n" + ("="*60))

print("\n\n\t⭐ DEMO 1 - Chunk Indices\n" + ("-"*60) + "\n")
for start, stop in chunk_indices(20, 6):
    print("\t", len(r := range(start, stop)), r)

print("\n" + ("="*60) + "\n\n\n")

# python multiprocess_queue.py a9d1cbf71942327e98b40cf5ef38a960
    