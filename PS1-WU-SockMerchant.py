# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_count = 0

    while ar:
        try:
            current_sock = ar[0]
            match_sock_index = ar.index(current_sock, 1)
            sock_count += 1
            ar.pop(match_sock_index)
            ar.pop(0)
        except ValueError:
            ar.pop(0)

    return sock_count



if __name__ == '__main__':
    result = sockMerchant(7, [10,20,20,10,10,30,50,10,20])
    print(result)