from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 12, 30)

# Generate the commits for "HELLO"
current_date = start_date
letters = "HELLO"

while current_date <= end_date:
    for letter in letters:
        # Create a commit message with the letter
        print(f"Committing letter '{letter}' on {current_date.strftime('%Y-%m-%d')}")
        # Simulate commit action (In real scenarios, the commit to the repository would happen here)
        current_date += timedelta(days=1)
        # Add a day gap for the spacing between letters' column
        current_date += timedelta(days=1) 
    # Move to the next day before the next letter
    current_date += timedelta(days=1)