import yaml
import os
with open('input.yaml', 'r')as file:
	data = yaml.safe_load(file)

#Set Output Variable
output_value = data.get('R_VERSION')
print(f'::set-output name=output_variable::{output_value}')
os.environ['RVERSION'] = data['R_VERSION']
