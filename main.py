from plyer import notification
import time


if __name__=='__main__':
    while True:
        notification.notify(
        title='Please Drink Water Now !!',
        message='To prevent dehydration, you need to drink adequate amounts of water. There are many different opinions on how much water you should be drinking every day.',
        app_icon="C:\\Users\\Daya\\PycharmProjects\DrinkWaterNotifier\icon.ico.ico",
        timeout=5
    )
        time.sleep(60*60) #every hour this will notify

# open terminal and run as pythonw .\main.py to run this program in the background