import sys
import os

# Add the project root directory to sys.path to allow importing from `src`
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.core.schema_versioning import SchemaVersioning
from src.utils.validators import is_required, is_type

schema_v1 = {
    "name": [is_required, is_type(str)],
    "age": [is_required, is_type(int)],
}

schema_v2 = {
    "name": [is_required, is_type(str)],
    "age": [is_required, is_type(int)],
    "email": [is_required, is_type(str)],
}

data = {"name": "John Doe", "age": 30, "email": "john@example.com"}

versioning = SchemaVersioning()
versioning.register_schema("v1", schema_v1)
versioning.register_schema("v2", schema_v2)

validated_data = versioning.validate_with_version("v2", data)
print("Validated data (v2):", validated_data)
