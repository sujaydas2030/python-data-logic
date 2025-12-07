#Agriculture Monitoring System
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval
# Taking the input
sensors_data = literal_eval(input())
def combine_sensor_data_corrected(sensors_data):
    total_sums = {}
    topic_counts = {}
    for each_set in sensors_data:
        for topic, value in each_set.items():
            total_sums[topic] = total_sums.get(topic, 0) + value
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

    # Calculate averages
    average_mappings = {}
    for topic, total_sum in total_sums.items():
        if topic_counts[topic] > 0:
            average_mappings[topic] = total_sum / topic_counts[topic]
        else:
            average_mappings[topic] = 0

    # Construct the final tuple in the desired order
    # Assuming the desired order is 'light intensity', 'temperature', 'humidity'
    final = (
        average_mappings.get('light intensity'),
        average_mappings.get('temperature'),
        average_mappings.get('humidity')
    )
    return final

# Print the output
print(combine_sensor_data_corrected(sensors_data))
