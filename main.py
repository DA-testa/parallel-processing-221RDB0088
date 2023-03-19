def parallel_processing(n, m, data):
    threads = [0] * n  #list to hold the finish time of each thread
    result = []  #list to hold the output
    for i in range(m):
        next_thread = 0
        for j in range(1, n):
            if threads[j] < threads[next_thread]:
                next_thread = j
        result.append((next_thread, threads[next_thread]))
        threads[next_thread] += data[i]

    return result

def main():
    #get inputs
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    #run the function
    result = parallel_processing(n, m, data)

    #print  results
    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
