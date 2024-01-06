from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def calculate_order(components):
    part_prices = {
        "A": 10.28, "B": 24.07, "C": 33.30,
        "D": 25.94, "E": 32.39,
        "F": 18.77, "G": 15.13, "H": 20.00,
        "I": 42.31, "J": 45.00,
        "K": 45.00, "L": 30.00,
    }
    total_price = 0
    selected_parts = []

    for component in components:
        if component in part_prices:
            total_price += part_prices[component]
            selected_parts.append(get_part_name(component))

    return total_price, selected_parts

def get_part_name(component):
    part_names = {
        "A": "LED Screen", "B": "OLED Screen", "C": "AMOLED Screen",
        "D": "Wide-Angle Camera", "E": "Ultra-Wide-Angle Camera",
        "F": "USB-C Port", "G": "Micro-USB Port", "H": "Lightning Port",
        "I": "Android OS", "J": "iOS OS",
        "K": "Metallic Body", "L": "Plastic Body",
    }
    return part_names.get(component, "")


@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            components = data.get("components", [])
            if not is_valid_order(components):
                return JsonResponse({"error": "Invalid order components"}, status=400)
            total_price, selected_parts = calculate_order(components)

            order_id = "order_id"  
            response_data = {
                "order_id": order_id,
                "total": round(total_price, 2),
                "parts": selected_parts,
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format in the request body"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


def is_valid_order(components):
    part_categories = {
        "Screen": {"A", "B", "C"},
        "Camera": {"D", "E"},
        "Port": {"F", "G", "H"},
        "OS": {"I", "J"},
        "Body": {"K", "L"},
    }
    part_counts = {category: 0 for category in part_categories}
    for component in components:
        for category, parts in part_categories.items():
            if component in parts:
                part_counts[category] += 1
    return all(count == 1 for count in part_counts.values())

