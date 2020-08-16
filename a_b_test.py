#import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# Main table
views_by_ad=\
ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views_by_ad)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source =\
ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

num_test = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

clicks_by_test = \
ad_clicks.groupby(['is_click','experimental_group']).user_id.count().reset_index()

a_clicks = ad_clicks[ad_clicks['experimental_group']=='A']
b_clicks = ad_clicks[ad_clicks['experimental_group']=='B']

# Pivot table
clicks_pivot = clicks_by_source.pivot(columns='is_click',index='utm_source',values='user_id').reset_index() 
#always try restructuring pivot
clicks_pivot['percent_clicked'] =\
clicks_pivot[True] / (clicks_pivot[True]+clicks_pivot[False])

clicks_by_test_piv = \
clicks_by_test.pivot(columns='is_click',index='experimental_group',values='user_id').reset_index()

clicks_by_test_piv['percentage_clicked'] = \
clicks_by_test_piv[True]/(clicks_by_test_piv[False]+clicks_by_test_piv[True])

a_clicks_day_piv = a_clicks.groupby(['day','is_click']).user_id.count().reset_index().pivot(columns='is_click',index='day',values='user_id').reset_index()
a_clicks_day_piv['percentage_clicked_a']=\
a_clicks_day_piv[True]/(a_clicks_day_piv[False]+a_clicks_day_piv[True])

b_clicks_day_piv = b_clicks.groupby(['day','is_click']).user_id.count().reset_index().pivot(columns='is_click',index='day',values='user_id').reset_index()
b_clicks_day_piv['percentage_clicked_b']=\
b_clicks_day_piv[True]/(b_clicks_day_piv[False]+b_clicks_day_piv[True])
#print(clicks_by_source)
#print(num_test)
#print(clicks_by_test_piv)
#print(clicks_pivot)
print(a_clicks_day_piv)
print(b_clicks_day_piv)
