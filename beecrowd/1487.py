def main():
    inst = 0
    while True:
        N, T =  map(int, input().split())
        if N == 0:
            return
        rides = [0] * N
        score_at_time = [0] * (T + 1)
        for i in range(N):
            # reads duration, score of each ride
            rides[i] = map(int, input().split()) 
        for ride in rides: 
            d, p = ride 
            for t in range(T + 1):
                if t + d > T: # time exceeded
                    break 
                elif score_at_time[t + d] < score_at_time[t] + p:
                    score_at_time[t + d] = score_at_time[t] + p
        inst += 1
        print('Instancia {}\n{}\n'.format(inst, score_at_time[T]))
        

if __name__ == "__main__":
    main()

