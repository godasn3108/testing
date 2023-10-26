import yaml

with open('input.yaml', 'r')as file:
	data = yaml.safe_load(file)

#Set Output Variable
output_value = data.get('R_VERSION')
print(f"::set-output name=R_VERSION::{output_value}")
