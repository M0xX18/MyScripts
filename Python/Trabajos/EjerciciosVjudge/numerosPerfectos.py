def numero_perfecto(num):
  sum = 0
  for i in range(1, num // 2 + 1):
    if num % i == 0:
      sum += i

  return sum == num

def main():
  lim_ite = int(input())

  for i in range(1, lim_ite + 1):
    if numero_perfecto(i):
      print(i, end=" ")

main()
