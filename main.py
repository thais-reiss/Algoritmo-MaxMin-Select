def max_min(arr, inicio, fim):

    if inicio == fim:
        return [arr[inicio], arr[inicio]]
    
    if fim == inicio + 1:
        if arr[inicio] < arr[fim]:
            return [arr[inicio], arr[fim]]
        else:
            return [arr[fim], arr[inicio]]
        
    meio = (inicio + fim) // 2

    arr1 = max_min(arr, inicio, meio)
    arr2 = max_min(arr, meio + 1, fim)
   
 
    min_val = min(arr1[0], arr2[0])
    max_val = max(arr1[1], arr2[1])
    
    return [min_val, max_val]

def main():
    array = [8,1,6,3,7]
    resultado = max_min(array, 0, len(array) - 1)
    print(f"Mínimo: {resultado[0]}; Máximo: {resultado[1]}")

if __name__ == "__main__":
    main()