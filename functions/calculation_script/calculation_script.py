import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def my_function(param1, param2):
    print(f"Starting the function with param1={param1}, param2={param2}")
    result = param1 + param2
    print(f"Calculation result: {result}")
    return result

def my_function_extended(param1, param2, param3, param4):
    result = param1 + param2 + param3 + param4
    return result