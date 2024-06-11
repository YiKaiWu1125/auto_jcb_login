import datetime
import time
import threading

def task_1():
    print("執行 Task 1 的特定程式碼")

def task_2():
    print("執行 Task 2 的特定程式碼")

def task_3():
    print("執行 Task 3 的特定程式碼")

def schedule_task(tasks):
    def check_task(task):
        name, target_time, task_function = task
        while True:
            current_time = datetime.datetime.now()
            time_difference = (target_time - current_time).total_seconds()

            if time_difference <= 0:
                print(f"執行 {name}")
                task_function()
                break
            elif time_difference <= 60:
                time.sleep(1)  # 當剩餘時間少於1分鐘時，每秒檢查一次
            else:
                time.sleep(60)  # 否則，每分鐘檢查一次

    threads = []
    for task in tasks:
        thread = threading.Thread(target=check_task, args=(task,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

# 設定多組任務，以下為範例
tasks = [
    ("Task 1", datetime.datetime(2024, 6, 11, 16, 53, 0), task_1),
    ("Task 2", datetime.datetime(2024, 6, 11, 16, 54, 0), task_2),
    ("Task 3", datetime.datetime(2024, 6, 11, 16, 55, 0), task_3),
]

schedule_task(tasks)
