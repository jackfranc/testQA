from statistics import fmean, mean, median
from typing import List, Union

def analyze_data(data: List[Union[int, float]]) -> dict:
   
    numeric_data = [x for x in data if x is not None]
    
    if not numeric_data:
        return {
            'Minimum': None,
            'Maximum': None,
            'Average': None,
            'Unique Values Count': 0,
            'Median': None,
        }

    minimum = min(numeric_data)
    maximum = max(numeric_data)

    if all(isinstance(x, int) for x in numeric_data):
        average = round(mean(numeric_data), 1)
    else:
        average = round(fmean(numeric_data), 1)

    unique_values_count = len(set(numeric_data))
    median_value = median(numeric_data)

    return {
        'Minimum': minimum,
        'Maximum': maximum,
        'Average': average,
        'Unique Values Count': unique_values_count,
        'Median': median_value,
    }
