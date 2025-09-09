def main():
    # YOUR CODE FOR PART 1 GOES HERE  
    cost_per_item = 19.99
    quantity = 5 
    subtotal=cost_per_item*quantity
    tax=subtotal*.13
    total=tax+subtotal
    
    # YOUR CODE FOR PART 2 GOES HERE
    print(f"cost_per_item = ${cost_per_item:0.2f}")
    print(f"quantity = {quantity}")
    print(f'subtotal_cost = ${subtotal:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total = ${total:0.2f}')

    # THIS IS THE CODE FOR PART 3
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print('After 5 years, your investment will be worth'+str(investment)+'dollars.')
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.

if __name__ == "__main__":
    main()