cf = 250000

# usuarios = [736,1500,3000,4000,5500,8000,10000]
# for usu in usuarios:
#         print((usu*11.292*12 - cf))

Q = [-150300,-46750,156500,292000,495300,834000,1105000,1105000,1105000,1105000]

A = 247823

interes = 0.520761813

total = 0
tirs = []

for i in range(0,10):
        total += Q[i] / (1+interes)**(i+1)

print(-A + total)

