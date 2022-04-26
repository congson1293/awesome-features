import yaml
from pathlib import Path

here = Path(__file__).parent.resolve()

def read_value(key:str):
    with open(f"{here}/resources/myresource.yaml", "r") as stream:
        try:
            dict = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)    
    return dict.get(key)

## test
# print(read_value('Key1')) # Value1