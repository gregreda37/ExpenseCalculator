def main():
    print("Computing your gasoline expenses...")
    total_miles = float(input("Total miles driven: ")) 

    while total_miles < 0 :
        total_miles = float(input("Enter a value > 0: ")) 
    
    total_miles_highway = float(input("Percentage of miles driven on highway (0-100) ")) 
    
    while total_miles_highway <= 0 or total_miles_highway >= 100 :
        total_miles_highway = float(input("Enter a value >= 0.0, and <= 100.0: ")) 
    
    gas_consumption = total_gallons(total_miles,total_miles_highway)
    gas_cost = gas_expense(gas_consumption)

    print("Here is the information for your trip:")
    print("Total miles: ",total_miles)
    print("Gas consumption:", round(gas_consumption,1))
    print("Gas expense:",gas_cost)
    
    new_trip = str(input("Compute gas expense for another trip (y or n)? ")) 
    if new_trip == "y":
        main()

def total_gallons(total_miles,total_miles_highway):
    miles_highway = (total_miles_highway * .01) * total_miles
    miles_city = (1-(total_miles_highway * .01)) * total_miles

    num_gallons = ((miles_highway/38) + (miles_city/28))
    

    return num_gallons


def gas_expense(num_gallons):
    gas_price = 2.69
    
    gas_expense = (num_gallons * gas_price)
    gas = round(gas_expense,2)
    dollar = ('${:,.2f}'.format(gas))

    return dollar





main()
