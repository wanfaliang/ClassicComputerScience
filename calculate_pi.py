def calculate_pi(n_precision):
    operator = 1.0
    denominator = 4.0
    numerator = 1.0
    pi=0.0
    for _ in range(n_precision):
        pi+=operator * numerator / denominator
        operator*=-1.0
        denominator+=2.0
    return pi
    int_input = int(input('Please input precision you desire'))
    pi = calculate_pi(int_input)
    print(f'{int_input} precision of pi is {pi}.')
  
