import yaml


class MakeDynamicClassFromYaml:
    def __init__(self, class_name_input, yaml_file):
        self.yaml_file = yaml_file
        self.class_name = class_name_input
        self.process_yaml_file()

    def process_yaml_data(self, data):
        class_name = "DynamicClass"
        class_attributes = data.keys()

        dynamic_class = type(self.class_name, (object,), {attr: data[attr] for attr in class_attributes})

        instance = dynamic_class()

        for attr, value in data.items():
            setattr(instance, attr, value)

        return instance

    def process_nested_data(self, data, instance):
        for key, value in data.items():
            if key == "resources":
                # Check if the key is 'resources'
                if "request" in value:
                    # Check if 'request' is present under 'resources'
                    request_data = value["request"]
                    setattr(instance.resources, "request", request_data)
            elif isinstance(value, dict):
                nested_instance = self.process_yaml_data(value)
                setattr(instance, key, nested_instance)
            else:
                setattr(instance, key, value)

    def process_yaml_file(self):
        with open(self.yaml_file, 'r') as file:
            yaml_data = yaml.safe_load(file)

        instance = self.process_yaml_data(yaml_data)
        self.process_nested_data(yaml_data, instance)

        self.instance = instance


# YAML 파일 경로
yaml_file = 'values.yaml'

person = MakeDynamicClassFromYaml("person", yaml_file)
instance = person.instance

# 'resource.request' 값을 출력
print("person.resources.request:", instance.resources.requests)
