from datetime import datetime, timedelta
import os

# Start and end dates
start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 12, 30)

# Commit information
commit_dates = []

# Define the letters and their patterns
patterns = {
    'H': [(0, 0), (1, 0), (2, 2), (3, 0), (4, 0)],  # H: full columns 0,4; middle row 2
    'E': [(0, 0), (2, 0), (4, 0), (0, 4), (2, 4)],  # E: full column 0; rows 0,2,4 column 4
    'L': [(0, 0), (4, 0)],  # L: full column 0; row 4 column 4
    'O': [(0, 0), (4, 0), (0, 4), (4, 4), (1, 1), (1, 3), (3, 1), (3, 3)],  # O: full columns 0,4; rows 0,4 columns 1,3
}

# Function to create commits for each letter
for letter, positions in patterns.items():
    for position in positions:
        # Create commits for the position
        date = start_date
        while date <= end_date:
            for _ in range(10):  # 10 commits on that date
                commit_dates.append((date.strftime('%Y-%m-%d'), f'Commit for letter {letter}'))
            date += timedelta(days=7)  # 1 week spacing
    start_date += timedelta(days=12)  # 1 week for spacing between letters

# Output commit list
for commit_date, purpose in commit_dates:
    print(f'Commit Date: {commit_date} - Purpose: {purpose}')

# For executability
if __name__ == '__main__':
    print('Generating commits...')
