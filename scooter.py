def solution(finish, scooter):
    i = 0
    total = 0
    current =0 
    n = len(scooter)

    while current < finish:
        while i < n and scooter[i]< current:
            i +=1 
        if i == n:
            break
        ride_start = scooter[i]
        ride_end = min(ride_start + 10, finish)
        total += ride_end -  ride_start 
        current = ride_end

        if ride_end == ride_start:
            i +=1

    return total