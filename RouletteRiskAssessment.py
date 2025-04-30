import random

def simulate_roulette(bet, spins):
    outcomes = [random.randint(0, 36) for _ in range(spins)]
    wins = outcomes.count(bet)
    probability_of_win = wins / spins
    expected_return = (35 * probability_of_win) - ((1 - probability_of_win))
    risk = 1 - expected_return
    return risk

# Get user input
bet = int(input("Enter the number you want to bet on (0-36): "))
spins = int(input("Enter the number of spins: "))

# Calculate risk
risk = simulate_roulette(bet, spins)

# Print risk and explanation
print(f"The risk associated with betting on {bet} over {spins} spins is {risk}")
print("This risk number represents the potential loss you could experience when placing this bet.")
print("If the risk is close to 0, this means the expected return is high, and therefore the risk of losing money is low.")
print("If the risk is close to 1, this means the expected return is low, and therefore the risk of losing money is high.")
print("Please note that this risk number is based on a mathematical model and does not guarantee any outcomes. Always gamble responsibly.")
