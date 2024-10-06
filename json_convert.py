import json

def convert_json_to_jsonl(input_file, output_file):
    # Read the JSON file
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
    
    # Write to JSONL file
    with open(output_file, 'w') as jsonl_file:
        for item in data:
            json.dump(item, jsonl_file)
            jsonl_file.write('\n')

# Usage
if __name__ == "__main__":
    input_file = 'examples.json'
    output_file = 'examples.jsonl'
    convert_json_to_jsonl(input_file, output_file)
    print(f"Conversion complete. JSONL file saved as {output_file}")
