import time
import random
print("Готовий? У тебе є 3 секунди, щоб натиснути Enter,\n як тільки з'явиться повідомлення!")
time.sleep(3)  # коротка пауза перед стартом
seconds = random.randint(2, 5)
time.sleep(seconds)
print("Натискай Enter!")
start_time = time.time()
input()
end_time = time.time()
reaction_time = end_time - start_time
print(f"Твій час реакції: {reaction_time:.3f} секунд!")

