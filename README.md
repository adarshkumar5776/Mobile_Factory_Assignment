# Mobile Factory Code Challenge
The Mobile Factory Code Challenge involves creating a Django API to configure mobile devices. Customers select components like screens, cameras, and OS, ensuring one part from each category. The system calculates the total price without a database, using local memory for part details, ensuring a validated and priced order output.

## Code Explanation

### `calculate_order(components)`
This function calculates the total price and selected parts based on the provided components.

### `get_part_name(component)`
This utility function retrieves the name of a part based on its code.

### `create_order(request)`
This Django view function handles the POST request to create an order.

### `is_valid_order(components)`
This function checks if the order components are valid based on the requirement of having one part from each category.
