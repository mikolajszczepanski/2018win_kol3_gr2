if __name__ == "__main__":
    from flight import Env
    from multiprocessing import Pool
    import os


    def run(limit):
        test = Env(limit)
        while True:
            print(test.get_flight_info())
            print("Write STOP to end or give a number to change angle")
            inp = input() #it goes to new line so I can't use print(str,end='\r')
            if inp == "STOP":
                break
            try:
                test.plane.set_angle(float(inp))
            except Exception:
                pass
            os.system('clear')


    Pool(run(20))
