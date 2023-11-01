import yaml

# Read the YAML file
with open('input.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Convert the YAML content to a string
yaml_string = yaml.dump(data)

# Set the environment variable
print(f'::set-output name=setup::{yaml_string}')
