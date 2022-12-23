import utils
from utils import find_max
# import ecommerce.shipping
from ecommerce.shipping import calc_shipping

result = utils.kg_to_pounds(30)
print(result)

result2 = utils.pounds_to_kg(100)
print(result2)

numbers = [40, 50, 30]
max_no = find_max(numbers)
print(max_no)

# ecommerce.shipping.calc_shipping()
calc_shipping()