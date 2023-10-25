import yaml

with open('input.yaml', 'r')as file:
	data = yaml.safe.load(file, Loader=yaml.FullLoader)

#Set Output Variable
print(f"::set-output name=R_VERSION::{data['R_VERSION']}")
