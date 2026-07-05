import pandas as pd

def get_salary(role, city):
    # Read the CSV file
    df = pd.read_csv("data/salary.csv")

    # Search for the role and city
    result = df[
        (df["Role"].str.lower() == role.lower()) &
        (df["City"].str.lower() == city.lower())
    ]

    # Return the salary if found
    if not result.empty:
        return result.iloc[0]["Salary"]
    else:
        return "Salary information not found."


# Test the tool
if __name__ == "__main__":
    role = input("Enter Role: ")
    city = input("Enter City: ")

    salary = get_salary(role, city)

    print(f"\nAverage Salary: {salary}")