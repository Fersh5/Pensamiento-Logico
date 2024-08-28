# Dada una matriz de enteros nums, mueva todos 0los ' al final de la misma mientras mantiene el orden relativo de los elementos distintos de cero.

# Tenga en cuenta que debe hacer esto en el lugar sin hacer una copia de la matriz.

 

# Ejemplo 1:

# Entrada: nums = [0,1,0,3,12]
#  Salida: [1,3,12,0,0]
# Ejemplo 2:

# Entrada: nums = [0]
#  Salida: [0]

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in range(len(nums)-1,-1,-1):
            if nums[num] == 0:
                nums.append(nums.pop(num))
        print(nums)

cas_1 = Solution()
cas_1.moveZeroes([0,0,1,2])

