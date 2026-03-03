import datetime
import random

# Function to generate backdated commits

def generate_backdated_commits():
    start_date = datetime.datetime(2025, 3, 1)
    end_date = datetime.datetime(2025, 12, 30)
    delta = datetime.timedelta(days=1)
    letters = 'HELLO'

    current_date = start_date
    while current_date <= end_date:
        for letter in letters:
            for _ in range(10):
                # Generate a random time for the commit
                commit_time = current_date + datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
                commit_message = f'Commit for letter {letter} on {commit_time.strftime("%Y-%m-%d %H:%M:%S")}'
                print(commit_message)  # Here you would perform the commit logic
        current_date += delta

# Call the function
if __name__ == '__main__':
    generate_backdated_commits()