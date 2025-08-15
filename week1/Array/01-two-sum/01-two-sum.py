from typing import List

# Solução Principal: Abordagem com Hash Map (Dicionário) - O(n) tempo, O(n) espaço
# Explicação: Percorremos o array uma vez, armazenando em um dicionário o valor e seu índice.
# Para cada número, verificamos se o complemento (target - num) já está no dicionário.
# Se sim, retornamos os índices. Isso garante eficiência, evitando loops aninhados.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dicionário para armazenar valor: índice
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        
        # Como garantido que há exatamente uma solução, não precisamos de retorno de erro
        return []

# Solução Alternativa: Abordagem de Força Bruta - O(n²) tempo, O(1) espaço
# Explicação: Usamos dois loops aninhados para verificar todas as pares possíveis.
# Isso é simples, mas ineficiente para arrays grandes, como pedido no follow-up para melhorar.
# Usado como alternativa para comparação.
class SolutionBrute:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Seção de Testcases
# Os testcases são baseados nos exemplos fornecidos no problema.
# Podemos executá-los para validar as soluções.

def run_tests():
    solution = Solution()
    solution_brute = SolutionBrute()
    
    # Testcase 1
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1]
    assert solution_brute.twoSum(nums, target) == [0, 1]
    
    # Testcase 2
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]
    assert solution_brute.twoSum(nums, target) == [1, 2]
    
    # Testcase 3
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1]
    assert solution_brute.twoSum(nums, target) == [0, 1]
    
    print("Todos os testcases passaram!")

# Executar os testes se o arquivo for rodado diretamente
if __name__ == "__main__":
    run_tests()

# Observações adicionais:
# - A solução principal atende ao follow-up, com complexidade menor que O(n²).
# - Consideramos edge cases como arrays com elementos iguais (ex: [3,3]) e garantimos não usar o mesmo elemento duas vezes.
# - Boas práticas: Uso de typing para clareza, asserts para testes, e código conciso.