from Himpunan_Logic import Himpunan

# Testing semua functionality
S = Himpunan(1,2,3,4,5,6,7,8,9)
h1 = Himpunan(1, 2, 3)
h2 = Himpunan(3, 4, 5)

print(len(h1))           # Output: 3 
print(3 in h1)           # Output: True 
print(h1 == h2)          # Output: False 

h1 += 4                  # Menambah elemen 4 ke h1 
print(h1)                # Output: {1, 2, 3, 4} 

h3 = h1 / h2             # Irisan
print(h3)                # Output: {3, 4} 

h4 = h1 + h2             # Gabungan  
print(h4)                # Output: {1, 2, 3, 4, 5} 

h5 = h1 - h2             # Selisih
print(h5)                # Output: {1, 2} 

h6 = h1.Komplement(S)    # Komplement
print(h6)                # Output: {5, 6, 7, 8, 9} 

print(abs(h1))           # Output: 16 (karena 4 elements = 2^4 = 16 subsets) 
