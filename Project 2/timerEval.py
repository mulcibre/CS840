import time

numOfDataPoints = 100

#   data gathering step
times = [time.clock() for i in range(0,numOfDataPoints)]

durations = [times[i+1] - times[i] for i in range(0,numOfDataPoints-1)]

print durations