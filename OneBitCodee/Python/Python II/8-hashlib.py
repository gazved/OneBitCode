import hashlib

#print(hashlib.algorithms_available)

print(hashlib.algorithms_guaranteed)

#sha256
algoritm = hashlib.sha256()

print(algoritm.digest())

message = "A melhor forma de prever o futuro é criá-lo".encode()
algoritm.update(message)
print(algoritm.hexdigest())