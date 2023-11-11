import numpy as np
import tensorflow as tf
from tensorflow import keras

# 보상 구조 정의
REWARDS = {
    "forward": 1,  # 직진 보상
    "collision": -10,  # 충돌 시 패널티
    "wrong_direction": -5  # 올바르지 않은 방향으로 이동할 때 패널티
}

# 강화 학습 환경 클래스
class Environment:
    def __init__(self):
        self.state = np.random.rand(5)  # 초기 상태

    def step(self, action):
        if action == 0:  # 직진
            reward = REWARDS["forward"]
        elif action == 1:  # 좌회전
            reward = REWARDS["wrong_direction"]
        else:  # 정지
            reward = REWARDS["collision"]

        # 다음 상태 업데이트
        next_state = np.random.rand(5)  # 임의의 상태
        done = (reward == REWARDS["collision"])  # 충돌 시 에피소드 종료

        return next_state, reward, done

# 강화 학습 모델 정의
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(5,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(3, activation='softmax')  # 3가지 행동: 직진, 좌회전, 정지
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 강화 학습 루프
# 강화 학습 루프
env = Environment()
num_episodes = 1000
for episode in range(num_episodes):
    state = env.state
    done = False

    while not done:
        action_probs = model.predict(np.array([state]))
        action = np.argmax(action_probs)

        next_state, reward, done = env.step(action)

        # 강화 학습 모델 업데이트
        target = np.zeros((1, 3))
        target[0][action] = 1
        model.fit(np.array([state]), target, epochs=1, verbose=0)

        # 상태 업데이트
        state = next_state

    print(f"에피소드 {episode + 1} 완료")


# 학습된 모델 테스트
test_state = np.random.rand(5)  # 테스트를 위한 임의의 상태
action_probs = model.predict(np.array([test_state]))
action = np.argmax(action_probs)
if action == 0:
    print("자동차가 직진합니다.")
elif action == 1:
    print("자동차가 좌회전합니다.")
else:
    print("자동차가 정지합니다.")
