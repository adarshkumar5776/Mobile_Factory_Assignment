# Mobile Factory Code Challenge


## Code Explanation

### `calculate_order(components)`
This function calculates the total price and selected parts based on the provided components.

### `get_part_name(component)`
This utility function retrieves the name of a part based on its code.

### `create_order(request)`
This Django view function handles the POST request to create an order.

### `is_valid_order(components)`
This function checks if the order components are valid based on the requirement of having one part from each category.
