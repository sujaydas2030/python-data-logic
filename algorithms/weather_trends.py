"""
Identifies temperature trends.
"""
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
temperatures = literal_eval(input())

def identify_trends(temperatures):
    # Write your code here
  for temperature in temperatures:
    if len(temperature)!=2:
      return 'Invalid temperature data'
    a,b=temperature
    if not (isinstance(a,(int,float))and isinstance(b,(int,float))):
      return 'Invalid temperature data'
  final_list=[]
  for i in range(1,len(temperatures)):
    temperature=temperatures[i]
    previous_temperature=temperatures[i-1]
    coolest,hotest=temperature
    old_coolest,old_hotest=previous_temperature

    if abs(coolest-old_coolest)>5 or abs(hotest-old_hotest)>5:
      final_list.append("Extreme Weather")
    elif ((coolest>old_coolest) and (hotest>old_hotest)) and (abs(coolest-old_coolest)<5 or abs(hotest-old_hotest)<5):
      final_list.append("Warming")
    elif ((coolest<old_coolest) and (hotest<old_hotest)) and (abs(coolest-old_coolest)<5 or abs(hotest-old_hotest)<5):
      final_list.append("Cooling")
    else:
      final_list.append("Fluctuating")

  return final_list

# Print the output
print(identify_trends(temperatures))
