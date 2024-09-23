def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.05 * track_width  # closer to center
    marker_2 = 0.1 * track_width   # more lenient but still close to center
    marker_3 = 0.2 * track_width   # bound for centerline adherence

    # Strongly reward being as close to the center as possible
    if distance_from_center <= marker_1:
        reward = 1.5  # maximum reward for being very close to center
    elif distance_from_center <= marker_2:
        reward = 1.0  # high reward for being close to center
    elif distance_from_center <= marker_3:
        reward = 0.5  # some reward but further from the center
    else:
        reward = 1e-4  # heavy penalty for being too far from center

    return float(reward)
