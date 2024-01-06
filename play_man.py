import gymnasium as gym
import pynput.keyboard as keyboard


def onRelease(key):
    global action_value
    action_value = 0


def onPress(key):
    global action_value

    try:
        if key.char == 'a':  # 向左移动
            action_value = 3
        elif key.char == 'd':  # 向右移动
            action_value = 2
        elif key.char == 'w':  # 发球
            action_value = 1
    except AttributeError:
        pass


# 监听键盘
listener = keyboard.Listener(on_press=onPress, on_release=onRelease)
listener.start()

env = gym.make("ALE/Breakout-v5", render_mode="human", obs_type="rgb")
observation, info = env.reset()

action_value = 1

for _ in range(1000):
    action = action_value
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()