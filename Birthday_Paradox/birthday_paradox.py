####################
# Birthday paradox #
####################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Calculate probability
number_people = np.arange(0,100)
days = 365
prob = 1
prob_not = []
prob_yes = []
for i in number_people:
    individual = (days-i)/days
    prob = prob*individual
    prob_not.append(prob*100)
    prob_yes.append((1-prob)*100)
    # print('# of individuals: %d \t Prob_yes: %.4f \t Prob_not: %.4f' % 
    #       (i+1, prob_yes[i], prob_not[i]))

# Plot probabilities
plt.figure(figsize=(8,4.5))
plt.plot(number_people+1, prob_yes,
         label='Probability of a pair')
plt.plot(number_people+1, prob_not,
         label='Probability of no matching a pair')
plt.plot(22.7,50,'ro')
plt.hlines(y=50, xmin=0, xmax=22.7, linestyles='--')
plt.vlines(x=22.7, ymin=0, ymax=50, linestyles='--')
plt.text(24, 5, '~23')
plt.title('Probability of a pair of individuals be born at same day')
plt.xlabel('Individuals'), plt.ylabel('Probability (%)')
plt.legend(loc='center right')
plt.yticks(np.arange(0,110,10))
plt.xticks(np.arange(0,110,10))
plt.xlim(0, None)
plt.ylim(0, None)
plt.show()