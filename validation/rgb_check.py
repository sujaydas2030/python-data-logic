"""
Validates RGB values.
"""
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
rgb_values = literal_eval(input())

def check_colour_validity(rgb_values):
    errors = []
    red, green, blue = rgb_values
    if not (0 <= red <= 255):
        errors.append("Invalid R value")
    if not (0 <= green <= 255):
        errors.append("Invalid G value")
    if not (0 <= blue <= 255):
        errors.append("Invalid B value")
    if not errors:
        return "Valid RGB values"
    else:
        return "\n".join(errors)

# Print the output
print(check_colour_validity(rgb_values))
