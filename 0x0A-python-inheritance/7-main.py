#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

# bg.integer_validator("my_int", 12)
# bg.integer_validator("width", True)

# bg.integer_validator( )

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", (4,))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
