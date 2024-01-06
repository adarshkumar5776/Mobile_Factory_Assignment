# Mobile Factory 

## Description

The Mobile Factory Code Challenge involves creating a Django API to configure mobile devices. Customers select components like screens, cameras, and OS, ensuring one part from each category. The system calculates the total price without a database, using local memory for part details, ensuring a validated and priced order output.
## Functions

### `calculate_order(components)`

- Calculates the total price and selected parts based on the given components.
- Utilizes the `part_prices` dictionary to get the prices of each component.
- Adds up the prices of selected components and keeps track of the selected parts.
- Returns the total price and a list of selected parts.

### `get_part_name(component)`

- Provides the corresponding part name for a given component code.
- Uses the `part_names` dictionary to map component codes to part names.
- Returns the part name for a given component code.

### `create_order(request)`

- Handles the creation of a mobile order based on a POST request with a JSON body containing a list of components.
- Checks if the order is valid using the `is_valid_order` function.
- If the order is valid, calculates the total price and selected parts using `calculate_order`.
- Responds with a JSON object containing order details, including an order ID, total price, and selected parts.

### `is_valid_order(components)`

- Checks if a given list of components forms a valid mobile order.
- Ensures there is exactly one part selected from each category: Screen, Camera, Port, OS, and Body.
- Uses dictionaries to define valid categories and keeps track of the counts of selected components in each category.
- Returns `True` if the order is valid, and `False` otherwise.

## Usage

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mobile-factory-configurator.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Run Development Server
   ```bash
   python manage.py runserver

4. Create Mobile Order
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"components": ["I", "A", "D", "F", "K"]}' http://localhost:8000/orders


