prime_numbers = []

for i in range (1,1001):
    if (i > 1):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            prime_numbers.append(i)
print("Prime Numbers between 1 and 1000:", prime_numbers)

max = 0
for i in range(len(prime_numbers)):
    for j in range(len(prime_numbers)-i-1):
        current_dif = prime_numbers[-i-1] - prime_numbers[j]
        if current_dif > max:
            max = current_dif

print("\n" + "Maximum difference of the Primes:", max)

# print( prime_numbers[-1] - prime_numbers[0] )

# Για τον υπολογισμο της μεγιστης διαφορας θα μπορουσα απλα να αφαιρεσω το πρωτο στοιχειο του πινακα  prime_numbers απο το τελευταιο
# με την εντολη print( prime_numbers[-1] - prime_numbers[0] ), την οποια εχω και στο απο πανω σχολιο

