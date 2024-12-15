import openai
import time
import csv
import argparse
from experiment_data import experiment_data  # Import the updated data

# Load the API key from a file
def load_openai_key():
    with open("openai_key", "r") as file:
        return file.read().strip()

# Function for GPT-4 query
def ask_gpt(system_prompt, user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=1  # Set temperature to 1
    )
    return response['choices'][0]['message']['content'].strip()

# Function to write a row to the CSV file
def write_row(file_name, treatment_name, estimated_market_value, willingness_to_pay):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([treatment_name, estimated_market_value, willingness_to_pay])

# Function to write the header row to the CSV file
def write_header(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Treatment', 'Market_Value_Estimation', 'Willingness_to_Pay'])


# Function to run the experiment
def run_experiment(file_name):
    # Load the API key
    api_key = load_openai_key()
    openai.api_key = api_key

    # System prompt for the participant
    system_prompt = (
        "You are participating in an experiment where you need to evaluate a property. "
        "Respond only with a number and no additional explanations."
    )

    # Write the header row
    write_header(file_name)

    # Iterate through the different anchor prices (treatments)
    for treatment in experiment_data["treatments"]:
        start_price = treatment["start_price"]
        treatment_name = treatment["treatment_name"]
        print(f"Treatment: {treatment_name}, Starting Price: {start_price}")

        for round_num in range(1, experiment_data["rounds"] + 1):
            print(f"Round {round_num}")

            # User prompt based on property data
            property_info = experiment_data["property"]
            user_prompt_market_value = (
                f"The seller has set a starting price of {start_price} euros for the property '{property_info['name']}' "
                f"located in {property_info['location']}. It is {property_info['size']} in size and was built in {property_info['year_built']}. "
                f"Property description: {property_info['description']} "
                f"What do you think is the realistic market value of this property?"
            )

            # Ask GPT-4 for the estimated market value
            estimated_market_value = ask_gpt(system_prompt, user_prompt_market_value)
            print(f"Estimated Market Value: {estimated_market_value}")

            # Add a delay to avoid hitting the rate limit
            time.sleep(1)

            # User prompt for willingness to pay
            user_prompt_payment = (
                f"Now that you have estimated the market value to be {estimated_market_value} euros: "
                f"How much would you be willing to pay for this property? "
                f"Please make sure your answer is realistic based on the estimated value. "
                f"Respond only with a number."
            )

            # Ask GPT-4 for willingness to pay
            willingness_to_pay = ask_gpt(system_prompt, user_prompt_payment)
            print(f"Willingness to Pay: {willingness_to_pay}")

            # Write the results to the CSV file
            write_row(file_name, treatment_name, estimated_market_value, willingness_to_pay)

            # Add a delay to avoid hitting the rate limit
            time.sleep(1)

# Start the experiment
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the GPT-4 anchor price experiment.')
    parser.add_argument('--file_name', type=str, default='experiment_results.csv', help='The name of the CSV file to save the results.')
    args = parser.parse_args()

    run_experiment(args.file_name)
