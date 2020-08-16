import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway,chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

#mean and standard deviation of rottweiler tail lengths
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print(np.mean(rottweiler_tl),np.std(rottweiler_tl))

whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

#returning the p val for a binomial test on whether whippets are more likely to be rescues (P(rescue) = 0.08)
print(num_whippet_rescues)
pval = binom_test(num_whippet_rescues,n=num_whippets,p=0.08)
print(pval)

whippet_weights = fetchmaker.get_weight("whippet")
terrier_weights = fetchmaker.get_weight("terrier")
pitbull_weights = fetchmaker.get_weight("pitbull")

breed_dataset = pd.concat([whippet_weights,terrier_weights,pitbull_weights])
breed_labels = ['whippets']*np.size(whippet_weights) + ['terriers']*np.size(terrier_weights) + ['pitbulls']*np.size(pitbull_weights)

#testing if there is a diff in the means of each group using an ANOVA test
t,pval = f_oneway(whippet_weights,terrier_weights,pitbull_weights)
print(pval)

t = pairwise_tukeyhsd(breed_dataset,breed_labels)
print(t)

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

colors_df = pd.DataFrame(pd.concat([poodle_colors,shihtzu_colors]).reset_index())

colors_df['breed'] = ['poodle']*np.size(poodle_colors)+['shihtzu']*np.size(shihtzu_colors)

color_table_temp = colors_df.groupby(['color','breed']).index.count().reset_index()

color_table = color_table_temp.pivot(columns='breed',index='color',values='index')

print(color_table)

t,pval2,_,__ = chi2_contingency(color_table)

print(pval2)
