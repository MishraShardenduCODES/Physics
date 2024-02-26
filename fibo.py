def fibo(num):
  if(num == 0 or num == 1):
    return num
  else:
    return fibo(num-1) + fibo(num-2)
