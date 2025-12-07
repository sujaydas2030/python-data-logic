"""
Formats name and birthdate. Accessing data from a tuple.
"""
# Take the input
data = input()

def export_data_in_format(data):
    # Write your code here
    final_dict={}
    data=data.strip("()")
    cleaned_data= tuple((map(str.strip,data.split(","))))
    first_name,last_name, year, month, day= cleaned_data[0].strip("'"),cleaned_data[1].strip("'"),int(cleaned_data[2]), int(cleaned_data[3]), int(cleaned_data[4])
    name= first_name+" "+last_name
    dob=f'{day:02d}-{month:02d}-{year}'
    final_dict={
        'full_name':name,
        'birthdate':dob
    }
    return final_dict

# Print the output
print(export_data_in_format(data))
