# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%

total_tasks = 20
score = int(input("How many tasks did you complete correctly? "))  # Liczba poprawnie rozwiązanych zadań
test_passed = False

# Obliczamy połowę liczby zadań
half_of_total = total_tasks / 2

# Warunek do sprawdzenia, czy użytkownik wykonał co najmniej 50% zadań
if score >= half_of_total:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
