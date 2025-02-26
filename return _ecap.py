def calculate_total(price, quantity, discount=0):
    total_before_discount = price * quantity
    total_after_discount = total_before_discount - discount
    
    print(f"Price per item: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total before discount: ${total_before_discount}")
    if discount > 0:
        print(f"Discount applied: ${discount}")
    else:
        print("No discount applied.")
    print(f"Total after discount: ${total_after_discount}")
    
    return total_after_discount

# With discount
print("\n--- With Discount ---")
c = calculate_total(price=30, quantity=2, discount=10)
print(f"Final total: ${c}\n")

# Without discount
print("\n--- Without Discount ---")
c = calculate_total(price=20, quantity=1)
print(f"Final total: ${c}")
