import sys
import os

# Add the project root directory to sys.path to allow importing from `src`
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.core.validator import SchemaValidator
from src.utils.validators import is_required, is_type, is_email

schema = {
    "user": {
        "name": [is_required, is_type(str)],  
        "details": {
            "age": [is_required, is_type(int)], 
            "email": [is_required, is_email],   
        },
    }
}

data = {
    "user": {
        "name": "John",
        "details": {
            "age": "test",
            "email": "john@example.com"
        }
    }
}

validator = SchemaValidator(schema)

try:
    validated_data = validator.validate(data)
    print("Validation successful:", validated_data)
except Exception as e:
    print("Validation error:", e)
