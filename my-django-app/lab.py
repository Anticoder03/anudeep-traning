import time

def calculate_typing_speed():
    print("\nStart typing the paragraph below and press Enter when done:\n")
    
    # ? Start the timer
    start_time = time.time()
    
    # Taking user input for typing
    typed_text = input()
    
    # End the timer
    end_time = time.time()
    
    # Calculate the time taken in seconds
    time_taken = end_time - start_time
    
    # Calculate the number of words typed
    word_count = len(typed_text.split())
    
    # Calculate typing speed in words per minute (WPM)
    typing_speed = (word_count / time_taken) * 60
    
    print(f"\nYou typed {word_count} words in {time_taken:.2f} seconds.")
    print(f"Your typing speed is {typing_speed:.2f} words per minute.")

# Call the function to calculate typing speed
calculate_typing_speed()

print("\nThank you for using the typing speed calculator!")