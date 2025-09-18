# Escriba un programa donde se calcule la sumatoria de todos los numeros desde 1 hasta n.

# Solucion con loops
def sum_of_numbers_with_loop(superior_limit_n : int) -> int :
    sum_of_all_numbers = 0
    for i in range(superior_limit_n + 1):
        sum_of_all_numbers += i
    return sum_of_all_numbers

print(f"The sum of the numbers with loop is: {sum_of_numbers_with_loop(100)}")

# Solucion sin loops

def sum_of_numbers_without_loop(superior_limit_n : int) -> int :
    sum_of_all_numbers = 0
    sum_of_all_numbers = int ( superior_limit_n * ( superior_limit_n + 1) / 2 )
    return sum_of_all_numbers

print(f"The sum of the numbers without loop is: {sum_of_numbers_without_loop(100)}")
