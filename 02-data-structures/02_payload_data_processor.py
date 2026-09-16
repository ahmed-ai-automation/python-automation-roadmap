"""
Module: 02_payload_data_processor.py
Description: Data structures manipulation simulating nested JSON/API payload handling.
Unit: 02 - Python Data Structures
"""

# --- 1. Dictionaries & Nested Data Structures (API Payload Simulation) ---
raw_customer_payload = {
    "customer_id": 1024,
    "name": "Ahmed Hassan",
    "email": "ahmed@example.com",
    "status": "active",
    "tags": ["lead", "vip", "lead"],  # Duplicate tags from API
    "orders": [
        {"order_id": "ORD-001", "amount": 150.0, "status": "completed"},
        {"order_id": "ORD-002", "amount": 450.5, "status": "pending"},
    ],
}

# Safely accessing nested fields using .get()
customer_name = raw_customer_payload.get("name", "Unknown")
customer_email = raw_customer_payload.get("email")

# --- 2. Sets (Deduplication & Set Operations) ---
# Remove duplicate tags automatically using a Set
raw_tags = raw_customer_payload.get("tags", [])
unique_tags = set(raw_tags)

# System permissions comparison using Set operations
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

missing_permissions = required_permissions.difference(user_permissions)
has_full_access = required_permissions.issubset(user_permissions)

# --- 3. Lists & Updates ---
# Extract orders list and add a new order using append()
orders_list = raw_customer_payload.get("orders", [])
new_order = {"order_id": "ORD-003", "amount": 200.0, "status": "completed"}
orders_list.append(new_order)

# --- 4. Tuples & Unpacking ---
# Function simulation returning multiple immutable values as a tuple
def get_payload_metrics(orders: list) -> tuple:
    total_count = len(orders)
    total_revenue = sum(order["amount"] for order in orders)
    return total_count, total_revenue

# Unpacking tuple values
order_count, total_revenue = get_payload_metrics(orders_list)

# --- 5. Structured Data Logging Output ---
log_divider = "-" * 50

print("=" * 50)
print(f"CUSTOMER PAYLOAD PROCESSED: {customer_name} ({customer_email})")
print("=" * 50)
print(f"Unique Tags Set      : {unique_tags}")
print(f"Total Orders Count   : {order_count}")
print(f"Total Revenue        : ${total_revenue:.2f}")
print(f"Missing Permissions  : {missing_permissions}")
print(f"Has Full System Access: {has_full_access}")
print(log_divider)
print("Updated Customer Payload Overview:")
print(f"Latest Order ID      : {orders_list[-1]['order_id']}")
print("=" * 50)