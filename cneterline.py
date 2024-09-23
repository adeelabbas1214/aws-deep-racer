def reward_function(params):
    # Extract parameters
    speed = params['speed']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = abs(params['steering_angle'])
    is_reversed = params['is_reversed']

    # Initialize the reward
    reward = 1.0

    # Reward for staying on track
    if all_wheels_on_track:
        reward += 10.0
    else:
        reward = 1e-3  # Low reward if off track

    # Reward for being in the center of the track
    marker = 0.1 * track_width
    if distance_from_center <= marker:
        reward += 10.0  # Closer to the center gives more reward
    else:
        reward += 1.0  # Slight reward for being further away but still on track

    # Reward for speed
    reward += speed * 10  # Higher speed gives a better reward

    # Reward for smooth steering
    if steering_angle < 15:  # Adjust this threshold as needed
        reward += 5.0  # Reward for smooth turns
    else:
        reward -= 1.0  # Penalize sharp turns

    # Penalize if the car is in reverse
    if is_reversed:
        reward *= 0.5  # Reduce reward if going in reverse

    return float(reward)
