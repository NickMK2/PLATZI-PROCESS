from enum import Enum

# The OrderStatus class is defined using the Enum class from the enum module. The OrderStatus class has five members: PENDING, SHIPPED, DELIVERED, ON_HOLD, and CANCELLED. The check_order_status function takes an OrderStatus object as an argument and returns a string based on the order status. The function uses if-elif-else statements to check the order status and return the corresponding string. The function is then called with different OrderStatus objects to test the implementation.

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    ON_HOLD = 4
    CANCELLED = 5
    
def check_order_status(status):
    if status == OrderStatus.PENDING:
        return "The order is pending"
    elif status == OrderStatus.SHIPPED:
        return "The order has been shipped"
    elif status == OrderStatus.DELIVERED:
        return "The order has been delivered"
    elif status == OrderStatus.ON_HOLD:
        return "The order is on hold"
    elif status == OrderStatus.CANCELLED:
        return "The order has been cancelled"
    else:
        return "Invalid order status"
    
# Output:
# The order is pending
# The order has been shipped
# The order has been delivered
# The order is on hold
# The order has been cancelled
# Invalid order status

print(check_order_status(OrderStatus.PENDING))
print(check_order_status(OrderStatus.SHIPPED))
print(check_order_status(OrderStatus.DELIVERED))    
print(check_order_status(OrderStatus.ON_HOLD))
print(check_order_status(OrderStatus.CANCELLED))
print(check_order_status(6))
