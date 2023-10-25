import yaml

with open('input.yaml', 'r')as file:
	data = yaml.load(file, Loader=yaml.FullLoader)

#Set Output Variable
print("***************************************************************"+data['R_VERSION'])
print(f"::set-output name=RVERSION::{data['R_VERSION']}")
