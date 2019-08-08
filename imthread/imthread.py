import threading

class multi_threading():
    def __init__(self, processing_func):
        self.process = processing_func

    def start(self, data):
        index_processed_data = {}
        def process_frames(data):
            #do some processing stuff============================
            processed_data = self.process(data[1])
            #====================================================

            #adding processed data to a list=====================
            index_processed_data.update({data[0]:processed_data})
            #====================================================

        threads = []
        for i in range(0,len(data)):
            # creating threads=================================================
            index_data = data[i]
            args = (i,index_data)
            t = threading.Thread(target=process_frames, name='t', args=(args,))
            #==================================================================

            # starting threads=================================================
            threads.append(t)
            t.start()
            #==================================================================

        #waiting for all the threads to finish
        for t in threads:
            t.join()
        #=====================================

        #sorting in the order the data was received====
        index = sorted(index_processed_data.keys())
        sorted_data = []
        for i in range(0, len(index)):
            #print(processed_frames[i])
            sorted_data.append(index_processed_data[i])
        #==============================================

        return sorted_data

