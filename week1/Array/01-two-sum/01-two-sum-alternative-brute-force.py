from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)  # Tamanho do array - print(f"Tamanho do array: {n}")
        
        for i in range(n):
            # Loop externo: para cada i
            print(f"Verificando índice {i} com valor {nums[i]}")  # Debug: início do loop i
            
            for j in range(i + 1, n):
                # Loop interno: para cada j > i
                sum_check = nums[i] + nums[j]  # Soma os dois
                print(f"Soma de {nums[i]} + {nums[j]} = {sum_check}")
                
                if sum_check == target:
                    # Encontrou a soma! Retorna índices
                    result = [i, j]  # Prepara resultado
                    print(f"Encontrado! Índices: {result}")
                    return result
        
        # Caso não encontre (mas problema garante uma solução)
        return []  # Retorno vazio (não deve ocorrer)

# Exemplo de uso (para debug)
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))  # Deve imprimir [0,1] com debugs