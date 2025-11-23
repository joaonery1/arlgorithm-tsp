class CaixeiroViajante:
    def __init__(self, distance_matrix, initial_city=0):
        self.dists = distance_matrix
        self.n = len(distance_matrix)
        self.initial_city = initial_city
        self.cache = {}

        self.FULL_VISITED = (self.n) - 1

    def tsp(self, visited_mask, current_city):

        if visited_mask == self.FULL_VISITED:
            return self.dists[current_city][self.initial_city]

        key = (visited_mask, current_city)
        if key in self.cache:
            return self.cache[key]

        best_cost = float('inf')

        for next_city in range(self.n):
            if (visited_mask & (1 << next_city)) == 0:
                new_cost = (
                    self.dists[current_city][next_city] +
                    self.tsp(visited_mask | (1 << next_city), next_city)
                )
                best_cost = min(best_cost, new_cost)

        self.cache[key] = best_cost
        return best_cost

if __name__ == "__main__":
    matriz = [
        # 0   1   2   3  
        [0,  10, 15, 20], # Saindo da cidade 0
        [10, 0,  35, 25], # Saindo da cidade 1
        [15, 35, 0,  30], # Saindo da cidade 2
        [20, 25, 30, 0]   # Saindo da cidade 3
    ]


    # 0 > 1 > 2 > 3 > 0 = 95
    # 0 > 2 > 1 > 3 > 0 = 95

    # 0 > 1 > 3 > 2 > 0
    # 10 + 25 + 30 + 15 = 80
    print("--- Teste 1: Começando da Cidade 0 ---")
    viajante1 = CaixeiroViajante(matriz, initial_city=0)
    custo1 = viajante1.tsp(visited_mask=1, current_city=0)
    print(f"Custo: {custo1}")
