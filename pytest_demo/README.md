# Demo Pytest

## Requirements
```
pip install -r requirements.txt
```

## Run 
### Run a specific test file
```
pytest test_pytest.py
```
### Run all test files
Name our test function with either ```test_<name>.py``` or ```<name>_test.py``` . Pytest will search for the file whose name ends or starts with ‘test’ and executes the functions whose name starts with ‘test’ within that file. 
```
pytest .
```