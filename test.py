import pandas as pd
import json

# Load the CSV file into a DataFrame
df = pd.read_csv('train_edit2.csv')

# Convert the DataFrame into a dictionary with the desired structure
# Convert each comment to a list
result_dict = df.set_index('img_name')['comments'].apply(lambda x: [x]).to_dict()

# Save the dictionary as a JSON file
with open('train_edit3.json', 'w') as json_file:
    json.dump(result_dict, json_file, indent=4)
