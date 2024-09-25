def optimal_merge(files):
    # Sort the files in ascending order
    files.sort()
    cost = 0
    while len(files) > 1:
        # Merge the smallest two files
        merged_file_size = files[0] + files[1]
        cost += merged_file_size
        # Replace the first file with the merged file size
        files[0] = merged_file_size
        # Remove the second file
        files.pop(1)
        # Sort the files again
        files.sort()
    return cost
files = [5, 10, 20, 30, 30]
min_cost = optimal_merge(files)
print("Minimum cost of merging is:", min_cost, "Comparisons")