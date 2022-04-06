"""
Simple calculator for calculating the cost of billing for ads on a fictional website.
The idea is that, $150 for 20 days.
We sell in multiples of 20 days; 20, 40, 60, 80 and so on.
However, if you insist on buying ads space for single days, 1 day costs $10.
"""

cost_of_ads = 150 #cost of ads if you buy in multiples of 20
extra_charge = 10 #cost of ads per day if not in multiples of 20. e.g 25 days would be 5*10.
total_ads_cost = 0

ads_duration = int(input("How many days do you want the ads to run?: "))

#ads_cost = cost_of_ads * (ads_duration/20)

plan1 = int(ads_duration/20) #get whole number of the ads duration
plan2 = ads_duration%20 #get the remainder of the duration
total_bill = (plan1 * cost_of_ads) + (plan2 * extra_charge) 
total_ads_cost += total_bill

print(f"Here is your billing summary:\nYou\'re ordering a {ads_duration} days ads at $150 for every 20 days\nand $10 for every additional day.")
print(f"Your Total ads cost is ${total_ads_cost} for {ads_duration} days.")
