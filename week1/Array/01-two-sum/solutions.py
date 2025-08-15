# Solução para o problema Two Sum (LeetCode)
# Objetivo: Encontrar índices de dois números em uma lista que somam um target dado.
# Assumindo exatamente uma solução única, sem usar o mesmo elemento duas vezes.

from typing import List

# Solução 1: Abordagem ingênua O(n^2) - Dois loops aninhados
# Esta solução verifica todas as pares possíveis, o que é simples mas ineficiente para arrays grandes.
class SolutionNaive:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):  # Loop externo: itera sobre cada elemento
            print(f"Verificando índice {i} com valor {nums[i]}")  # Print de debug: mostrando o elemento atual
            for j in range(i + 1, n):  # Loop interno: itera sobre elementos subsequentes para evitar duplicatas
                soma = nums[i] + nums[j]  # Calcula a soma dos dois elementos
                print(f"  - Par ({i}, {j}): soma = {soma}")  # Print de debug: exibindo o par e a soma
                if soma == target:  # Verifica se a soma é igual ao target
                    print(f"Solução encontrada: índices {i} e {j}")  # Print de debug: solução achada
                    return [i, j]  # Retorna os índices imediatamente
        return []  # Caso não encontre (embora assumimos que sempre há uma solução)

# Solução 2: Abordagem eficiente O(n) - Usando mapa de hash (dicionário)
# Esta é a solução otimizada, armazenando valores e índices em um dicionário para buscas O(1).
# Atende ao follow-up de complexidade menor que O(n^2).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Dicionário para armazenar valor: índice
        print("Inicializando hashmap vazio")  # Print de debug: início do mapa
        for i, num in enumerate(nums):  # Itera sobre o array com índice e valor
            complement = target - num  # Calcula o complemento necessário para atingir o target
            print(f"Índice {i}, valor {num}, complemento {complement}")  # Print de debug: detalhes da iteração
            if complement in hashmap:  # Verifica se o complemento já está no mapa
                print(f"Complemento encontrado no hashmap: índice {hashmap[complement]}")  # Print de debug: achou o par
                return [hashmap[complement], i]  # Retorna os índices (o do complemento primeiro)
            hashmap[num] = i  # Adiciona o valor atual ao mapa
            print(f"Adicionado ao hashmap: {num}: {i}")  # Print de debug: atualização do mapa
        return []  # Caso não encontre (embora assumimos que sempre há uma solução)

# Seção de Testcases
# Incluindo casos do LeetCode, casos de borda e cenários adicionais para validação.
# Testamos ambas as soluções para garantir consistência.

def run_tests():
    test_cases = [
        # Caso 1: Exemplo básico do LeetCode
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        # Caso 2: Outro exemplo com ordem não sequencial
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        # Caso 3: Duplicatas (mesmo valor em índices diferentes)
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        # Caso de borda: Array mínimo (tamanho 2), com negativos
        {"nums": [-1, -2], "target": -3, "expected": [0, 1]},
        # Caso de borda: Números grandes, perto dos limites das constraints
        {"nums": [10**9, -10**9, 0], "target": 0, "expected": [0, 1]},
        # Caso adicional: Array com mais elementos, solução no meio
        {"nums": [1, 3, 5, 7, 9], "target": 12, "expected": [2, 4]},
        # Caso de borda: Solução com primeiro e último elemento
        {"nums": [4, 5, 6, 7, 8], "target": 12, "expected": [0, 4]},
        # Caso inesperado: Array com zeros
        {"nums": [0, 0, 1, 2], "target": 0, "expected": [0, 1]},
        # Caso de falha potencial: Se houver duplicatas mas não usar mesmo índice
        {"nums": [1, 2, 1], "target": 2, "expected": [0, 2]},
    ]

    naive_solver = SolutionNaive()
    efficient_solver = Solution()

    for idx, case in enumerate(test_cases):
        print(f"\nTeste {idx + 1}: nums={case['nums']}, target={case['target']}")
        
        # Testando solução ingênua
        result_naive = naive_solver.twoSum(case['nums'], case['target'])
        print(f"Resultado Solução Ingênua: {result_naive}")
        assert sorted(result_naive) == sorted(case['expected']), f"Erro na Solução Ingênua: Esperado {case['expected']}, Obtido {result_naive}"
        
        # Testando solução eficiente
        result_efficient = efficient_solver.twoSum(case['nums'], case['target'])
        print(f"Resultado Solução Eficiente: {result_efficient}")
        assert sorted(result_efficient) == sorted(case['expected']), f"Erro na Solução Eficiente: Esperado {case['expected']}, Obtido {result_efficient}"
    
    print("\nTodos os testes passaram com sucesso!")

# Executar os testes
if __name__ == "__main__":
    run_tests()