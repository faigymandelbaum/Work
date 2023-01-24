import multiprocessing

def multiply(number1, number2, preaddressed_envelope):
    total = number1 * number2
    with preaddressed_envelope.get_lock():
        preaddressed_envelope.value += total


def main():

    preaddressed_envelope = multiprocessing.Value('i')

    multiply1 = multiprocessing.Process(target=multiply, args=[5,10,preaddressed_envelope])
    multiply2 = multiprocessing.Process(target=multiply, args=[4,8,preaddressed_envelope])

    multiply1.start()
    multiply2.start()

    multiply1.join()
    multiply2.join()

    print (preaddressed_envelope.value) 

if __name__ == '__main__':
    main()