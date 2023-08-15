import statistics

# Get user input as a string
input_string = input("Enter values separated by spaces: ")

# Split the input string into a list of values
input_list = input_string.split()

# Convert the list of strings to a list of floats
data = [float(value) for value in input_list]

# Calculate standard deviation and mean
std_deviation = statistics.stdev(data)
mean = statistics.mean(data)

# Calculate Z-score for each value
z_scores = [(value - mean) / std_deviation for value in data]

# Print Z-scores
for i, z_score in enumerate(z_scores):
    print(f"Z-score for value {data[i]}: {z_score:.2f}")

