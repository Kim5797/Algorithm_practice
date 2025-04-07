import time

# start = time.time()

while True:
    try:
        S = input()
        print(S)
    except EOFError:
        break