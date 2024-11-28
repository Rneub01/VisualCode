while True:
    outcome_a = input('What is outcome A: ')
    outcome_b = input('What is outcome B: ')

    var_1 = float(outcome_a)
    var_2 = float(outcome_b)

    outcome = 'Outcome A: {}'.format(outcome_a)
    outcome1 = 'Outcome B: {}'.format(outcome_b)

    Percentage_Outcome_A = (1/var_1)
    Percentage_Outcome_B = (1/var_2)
    Outcome_sum = (Percentage_Outcome_A + Percentage_Outcome_B)
    Arbitrage_percentage = (Percentage_Outcome_A + Percentage_Outcome_B) * 100

    is_an_Arbitrage = '{}%, This is an Arbitrage'
    is_not_an_Arbitrage = '{}% This is not an Arbitrage'

    if Arbitrage_percentage < 100:
        print(is_an_Arbitrage.format(Arbitrage_percentage))
    elif Arbitrage_percentage > 100:
        print(is_not_an_Arbitrage.format(Arbitrage_percentage))
        continue
        
    Investment = input('What is your Investment: ')
    Investment_var = int(Investment)
    Arbitrage_Profit = (Investment_var/Outcome_sum) - Investment_var
    
    profit_txt = 'Your profit is ${}'
    outcome_a_profit_txt = 'Outcome A Stake: ${}'
    outcome_b_profit_txt = 'Outcome B Stake: ${}'
    
    outcome_a_profit = (Investment_var * (Percentage_Outcome_A * 100)) / Arbitrage_percentage
    outcome_b_profit = (Investment_var * (Percentage_Outcome_B * 100)) / Arbitrage_percentage
    print(outcome_a_profit + outcome_b_profit)
    print(profit_txt.format(Arbitrage_Profit), outcome_a_profit_txt.format(outcome_a_profit), outcome_b_profit_txt.format(outcome_b_profit))