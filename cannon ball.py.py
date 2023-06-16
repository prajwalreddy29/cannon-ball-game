import math

def get_horizontal_distance(angle, velocity):
    radian_angle = math.radians(angle)
    time_of_flight = (2 * velocity * math.sin(radian_angle)) / 9.8
    horizontal_distance = velocity * math.cos(radian_angle) * time_of_flight
    return horizontal_distance

def play_game():
    target_distance = 100  # Distance to the target
    print("Welcome to the Cannon Game!")
    print("Try to hit the target {} meters away.".format(target_distance))

    while True:
        angle = float(input("Enter the angle (in degrees): "))
        velocity = float(input("Enter the velocity (in meters per second): "))

        distance = get_horizontal_distance(angle, velocity)

        if distance == target_distance:
            print("Congratulations! You hit the target!")
            break
        elif distance < target_distance:
            print("You missed! The cannonball fell short.")
        else:
            print("You missed! The cannonball went too far.")

play_game()
