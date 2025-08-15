from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dicionário para armazenar número e seu índice
        num_to_index = {}  # Inicializa dicionário vazio
        print(f"Inicializando dicionário vazio, {num_to_index=}")
        
        for i, num in enumerate(nums):
            # Calcula o complemento necessário para atingir o target
            complement = target - num  # Calcula complemento
            print(f"{num=} -> {target=}, {complement=}")
            
            # Verifica se o complemento já está no dicionário
            if complement in num_to_index:
                # Encontrou! Retorna os índices
                result = [num_to_index[complement], i]  # Prepara resultado
                print(f"Encontrou {complement=} in {num_to_index=}")
                print(f"{result=}")
                return result
            else:
                print(f"{complement=} não encontrado para {num=} em {num_to_index=}, continuando...")
            # Adiciona o número atual ao dicionário
            num_to_index[num] = i  # Adiciona ao dicionário
            print(f"Adicionando {num=} e índice {i=} ao dicionário {num_to_index=}")
        
        # Caso não encontre (mas problema garante uma solução)
        return []  # Retorno vazio (não deve ocorrer)

# Exemplo de uso (para debug)
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))  # Deve imprimir [0,1] com debugs
    print()
    print(sol.twoSum([3,2,4], 6))  # Deve imprimir [1,2] com debugs
    print()
    print(sol.twoSum([3,3], 6))  # Deve imprimir [0,1] com debugs