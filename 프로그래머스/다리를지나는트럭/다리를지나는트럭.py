


def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    total_weight = 0
    time = 0
    while truck_weights:
        # print(time, truck_weights)
        total_weight -= q.pop(0)
        if total_weight + truck_weights[0] <= weight:
            total_weight += truck_weights[0]
            q.append(truck_weights.pop(0))
        else:
            q.append(0)
        time += 1
    return time+bridge_length




bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))

