"""
Counts customer product purchases.
"""
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
purchases = literal_eval(input())

def get_customer_purchase_count(purchases):
    # Write your code here
  product_dictionaries={}
  inner_dictionary={}
  for customer_id,product in purchases:
    if customer_id not in product_dictionaries:
      product_dictionaries[customer_id]={}

    customer_products = product_dictionaries[customer_id]
    customer_products[product] = customer_products.get(product, 0) + 1

  return product_dictionaries


# Print the output
print(get_customer_purchase_count(purchases))
