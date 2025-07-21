def check_eligibility(score_percentage):
    if score_percentage >= 70:
        print("Eligible")
    else:
        print("Failed")

# Example usage:
check_eligibility(85)  # Output: Eligible
check_eligibility(65)  # Output: Failed
