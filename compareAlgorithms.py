import time
from sortingAlgorithms import orderArray

def main():

    v1=list(range(1,7))
    v2=list(range(10,10000,100))

    header="input array length"
    for k in v2:
        header = header + ";" + str(k) 

    f = open("result.csv", "w")
    
    for option in v1:        
        print(option)
        f.write(header + "\n")
        row=""
        row="time (ns) algorithm " + str(option)
        for n in v2:
            print(n)
            start = time.perf_counter_ns()
            orderArray(option,n)
            end = time.perf_counter_ns()
            lapse = end - start
            row = row + ";" + str(lapse)
        f.write(row + "\n\n")
    
    f.close()


if __name__=="__main__":
    main()
