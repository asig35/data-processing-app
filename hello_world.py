import pandas as pd

def process_data(data):
    """
    Process the provided data and export it to Excel.
    
    Args:
        data (dict): Dictionary containing lists of Names, Ages, and Cities
    """
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Export to Excel
    excel_file = 'hello_world.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"\nData has been exported to {excel_file}")

if __name__ == '__main__':
    # Sample data for testing
    test_data = {
        'Name': ['John', 'Alice', 'Bob'],
        'Age': [28, 24, 32],
        'City': ['New York', 'San Francisco', 'Chicago']
    }
    process_data(test_data) 