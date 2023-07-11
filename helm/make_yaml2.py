from ruamel.yaml import YAML
# python -m pip install ruamel.yaml

# Define the MakeDynamicClassFromYaml class
class MakeDynamicClassFromYaml:
    def __init__(self, name, yaml_file):
        self.name = name
        self.instance = self._create_instance(yaml_file)
        print( "self.instance : ", self.instance)

    def _create_instance(self, yaml_file):
        with open(yaml_file, 'r') as file:
            yaml = YAML(typ='safe')
            data = yaml.load(file)
            print(  "data:",   data)

        # Create a dynamic class instance with the YAML data
        cls = type(self.name, (), data)
        
        print ("cls:", cls)
        return cls()

# Specify the YAML file path
yaml_file = 'values.yaml'

# Create an instance of the MakeDynamicClassFromYaml class
person = MakeDynamicClassFromYaml("person", yaml_file)
instance = person.instance

print ( "person.instance:", instance)
print ( "person.instance type:", type(instance) )

# Dynamically set the value of resources.requests
instance.resources['requests'] = {'cpu': '500m', 'memory': '128Mi'}

# Save the updated YAML to a file
output_file = 'updated_values.yaml'

print( "instace_dict:",   instance.__dict__)

with open(output_file, 'w') as file:
    yaml = YAML()
    yaml.dump(instance.__dict__, file)

print(f"Updated YAML file saved to '{output_file}'.")