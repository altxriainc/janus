import sys
import os

# Add the project root directory to sys.path to allow importing from `src`
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.core.serializer import JSONSerializer, YAMLSerializer

data = {"name": "John Doe", "age": 30, "email": "john@example.com"}

json_serializer = JSONSerializer()
yaml_serializer = YAMLSerializer()

# JSON
json_data = json_serializer.serialize(data)
print("JSON Serialized:", json_data)
print("JSON Deserialized:", json_serializer.deserialize(json_data))

# YAML
yaml_data = yaml_serializer.serialize(data)
print("YAML Serialized:", yaml_data)
print("YAML Deserialized:", yaml_serializer.deserialize(yaml_data))
