result = 0

for open_value, high_value, low_value in zip(df['Open'], df['High'], df['Low']):
    if high_value > open_value:
        print(f"Open: {open_value} High: {high_value} Theoretical benefits: {high_value - open_value}")
        result += high_value - open_value
    else
        print(f"Open: {open_value} High: {high_value} Theoretical Loses: {open_value - low_value}")
        result -= high_value - open_value
        
    string_result = (lambda r: if r > 0: 'Positive' elif r < 0: 'Negative' else '')(result) 
    print(f"Final result is {string_result}: {result}")