import json

def beautify_json(input_file, output_file):
    # Read the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Beautify (pretty-print) the JSON and write to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    
    print(f"Beautified JSON has been written to {output_file}")

# Example usage
input_file = './captions_train2014.json'
output_file = './output.json'
beautify_json(input_file, output_file)
