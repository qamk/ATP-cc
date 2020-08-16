#import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
"""print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))"""

visits_cart = pd.merge(visits,cart,how='left')
print(visits_cart.head(5))
#2052 rows, 1652 NULL for cart_time
#i.e. 1652 people did not add to cart
print(visits_cart.info()) 

num_to_checkout = visits_cart['cart_time'].count() / float(2052)
print(num_to_checkout)
vis_car_che = pd.merge(visits_cart,checkout,how='left')
all_data = pd.merge(vis_car_che,purchase,how='left')
print(all_data.head(5))

checkout_purchase =\
1-(float(all_data['purchase_time'].count()) /\
all_data['checkout_time'].count())
print("Did not purchase after checkout {}".format(checkout_purchase))

cart_checkout =\
1-(float(all_data['checkout_time'].count()) /\
all_data['cart_time'].count())
print("Did not checkout after cart {}".format(cart_checkout))

visit_cart =\
1-(float(all_data['cart_time'].count()) /\
all_data['visit_time'].count())
print("Did not cart after visiting {}".format(visit_cart))

all_data['time_to_purchase'] =\
all_data['purchase_time'] - \
all_data['visit_time']

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
