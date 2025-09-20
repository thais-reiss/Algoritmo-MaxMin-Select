# Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select)
 ## O que é este projeto?
 Este projeto apresenta uma implementação em python do algoritmo de Seleção Simultânea do Maior e do Menor Elementos, bem como uma análise da complexidade assintótica pelo método da contagem de operações e também pela aplicação do Teorema Mestre.  

 ## O que é o algoritmo MaxMin Select?
Este algoritmo é um método para se encontrar o maior e o menor elementos de um conjunto de dados, utilizando a abordagem de dividir e conquistar. 
Este algoritmo divide um vetor recursivamente em duas partes menores. Em cada divisão, o algoritmo encontra o menor e o maior elementos de cada metade e, depois, combina os resultados, comparando apenas os dois menores e os dois maiores encontrados. A recursão continua até chegar aos casos base, que são vetores de tamanho 1 ou 2. 
A vantagen deste método é que ele diminui o número de comparações em relação a encontrar o mínimo e o máximo separadamente ou utilizando uma abordagem iterativa.

## Como rodar o projeto
Para rodar o projeto, é preciso ter o Python 3 instalado e uma IDE. A partir disso, execute no terminal o seguinte comando:
```bash
   python main.py
```
## Lógica da implementação

```python
def max_min(arr, inicio, fim):
```
A função começa recebendo três argumentos: 
1. arr - representa o array do qual os elementos máximo e mínimo serão extraídos.
2. inicio - representa o índice inicial do array.
3. fim - representa o índice final do array.
---

```python
    if inicio == fim:
        return [arr[inicio], arr[inicio]]
```
Caso base 1: quando o índice inicial é igual ao índice final, significa que o array tem apenas 1 elemento. Nesse caso, ele é retornado como o mínimo e o máximo. 

---


 
