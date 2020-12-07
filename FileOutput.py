# FileOutput prints to file the name of test, result and time it took to run test

class FileOutput:
    def __init__(self, test_run_information):
        self.test_run_information = test_run_information

    def log(self):
        f = open("output.log", "w")
        for test_run in self.test_run_information:
            f.write('%s: %s  %.5f ms \n' % (test_run[0], test_run[1], test_run[2]))
        f.close()
