import yaml


class MakeDynamicClassFromYaml:
    def __init__(self, class_name_input, yaml_file):
        self.yaml_file = yaml_file
        self.class_name = class_name_input
        self.process_yaml_file()
        
    def process_yaml_file(self):
        with open(self.yaml_file, 'r') as file:
            yaml_data = yaml.load(file, Loader=yaml.FullLoader)

        instance = self.process_yaml_data(yaml_data)
        self.process_nested_data(yaml_data, instance)

        self.instance = instance

    def process_yaml_data(self, data):
        class_name = "DynamicClass"
        class_attributes = data.keys()

        dynamic_class = type(self.class_name, (object,), {attr: data[attr] for attr in class_attributes})
        print( "dynamic_class", dynamic_class)
        instance = dynamic_class()

        for attr, value in data.items():
            setattr(instance, attr, value)

        return instance

    def process_nested_data(self, data, instance):
        for key, value in data.items():
            print(f"Processing key: {key}")

            if isinstance(value, dict):
                nested_data = self.process_yaml_data(value)
                setattr(instance, key, nested_data)
            else:
                setattr(instance, key, value)




# # YAML 파일 경로
#yaml_file = './data.yaml'
yaml_file = '/home/skycloud/cdktf/helm/data.yaml'


person = MakeDynamicClassFromYaml("person", yaml_file)
instance = person.instance
print("person.age:", instance.age)
# print("person.resources.request.cpu:", instance.resources.request["cpu"])
# print("person.resources.limit.cpu:", instance.resources.limit["cpu"])
# print("person.resources.request.two_depth.two_one:", instance.resources.request["two_depth"]["two_one"])
# print("person.resources.limit.two_depth.two_one:", instance.resources.limit["two_2depth"]["two_3usa"])
# print("person.resources.limit.two_depth.two_two.two_3korea:", instance.resources.limit["two_2depth"]["two_3korea"])
# print("person.resources.limit.two_depth.two_two.three_depth:", instance.resources.limit["two_2depth"]["two_4korea"])
# print("person.affinity.role:", instance.affinity.role)
# #print("person.resources.limit.two_depth.two_one:", instance.resources.limit.two_depth.two_one)
