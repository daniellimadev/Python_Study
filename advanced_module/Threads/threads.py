# (Part 3) Threads - Executing processing in parallel

from threading import Lock, Thread
from time import sleep

"""
class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.tempo = time

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MyThread('Thread 1', 5)
t1.start()

t2 = MyThread('Thread 2', 3)
t2.start()

t3 = MyThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(text, time):
    sleep(time)
    print(text)


t1 = Thread(target=vai_demorar, args=('Hello world 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Hello world 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Hello world 3!', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""


"""
def vai_demorar(text, time):
    sleep(time)
    print(text)


t1 = Thread(target=vai_demorar, args=('Hello world 1!', 10))
t1.start()
t1.join()

print('Thread is over!')
"""


class Tickets:
    """
    Class that sells tickets
    """

    def __init__(self, stock: int):
        """ Initializing...

        :param stock: number of tickets in stock
        """
        self.stock = stock
        # Our padlock
        self.lock = Lock()

    def buy(self, quantity: int):
        """
        Purchase a certain number of tickets

        :param quantity: The number of tickets you want to buy
        :type quantity: int
        :return: Nothing
        :rtype: None
        """
        # Lock the method
        self.lock.acquire()

        if self.stock < quantity:
            print("We don't have enough tickets.")
            # Release the method
            self.lock.release()
            return

        sleep(1)

        self.stock -= quantity
        print(f'You purchased {quantity} ticket(s). '
            f'We still have {self.stock} in stock.')

        # Release the method
        self.lock.release()


if __name__ == '__main__':
    tickets = Tickets(10)

    for i in range(1, 20):
        t = Thread(target=tickets.buy, args=(i,))
        t.start()

    print(tickets.stock)