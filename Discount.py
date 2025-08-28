# Function to calculate the final price after applying a discount.
# It takes the original price and discount percentage as arguments.
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price if the discount is applied, otherwise the original price.
    """
    # Check if the discount is 20% or higher.
    # The discount_percent is a number, so we check if it's greater than or equal to 20.
    if discount_percent >= 20:
        # Calculate the discount amount.
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price.
        final_price = price - discount_amount
        # Return the final price after the discount.
        return final_price
    else:
        # If the discount is less than 20%, return the original price.
        return price

# --- Main part of the program to get user input and run the function ---

# Use a try-except block to handle potential errors if the user enters non-numeric values.
try:
    # Prompt the user to enter the original price.
    # We use float() to convert the input string to a number that can have decimals.
    original_price = float(input("Enter the original price of the item: "))
    
    # Prompt the user to enter the discount percentage.
    discount_rate = float(input("Enter the discount percentage: "))

    # Call the calculate_discount function with the user's input.
    final_price = calculate_discount(original_price, discount_rate)

    # Check if the final price is different from the original price to determine
    # if a discount was applied.
    if final_price < original_price:
        # If a discount was applied, print the final price with a message.
        print(f"Final price after a {discount_rate}% discount: ${final_price:.2f}")
    else:
        # If no discount was applied, print the original price with a message.
        print(f"No discount applied. Original price: ${original_price:.2f}")

except ValueError:
    # If the user's input cannot be converted to a number, print an error message.
    print("Invalid input. Please enter valid numbers for price and discount.")