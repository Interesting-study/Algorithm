#배낭 수용가능량 : 15kg, ($4, 12kg), ($2, 1kg), ($10, 4kg), ($1, 1kg), ($2, 2kg)
def fractional_knapsack(cargo):
    capacity = 15
    pack = []

    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse = True)
    #pack(money, weight)
    #짐을 쪼갤 수 있으므로 단가순으로 배치함

    total_value:float = 0
    for p in pack:
        if capacity - p[2] >=0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction


cargo = [(4, 12),
         (2, 1),
         (10, 4),
         (1, 1),
         (2, 2)
]

r = fractional_knapsack(cargo)
