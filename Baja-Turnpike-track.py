def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']

    # Calculate 3 markers that are at varying distances from the centerline
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Initialize reward
    reward = 1e-3  # small reward by default

    # Reward for staying near the centerline
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed or close to off-track

    # Reward for higher speeds
    SPEED_THRESHOLD = 2.0  # m/s
    if speed > SPEED_THRESHOLD:
        reward += 0.5
    else:
        reward += 0.1

    # Bonus reward for progress towards the finish line
    REWARD_PROGRESS = 0.1
    reward += progress * REWARD_PROGRESS

    # Penalty for too many steps (to encourage faster completion)
    if steps > 300:
        reward *= 0.5

    return float(reward)
