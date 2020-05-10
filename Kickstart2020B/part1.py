def main():


    ##format input##
    testCases = int(input())
    Ns = [None]*testCases
    Hs = [None for x in range(testCases)]

    for case in range(testCases):
        Ns[case] = int(input())
        Hs[case] = [int(s) for s in input().split(" ")]

    caseNo = 1

    for case in range(testCases):
        runningTotal = 0
        N = Ns[case]
        Heights = Hs[case]
        for possPeak in range(1,N-1):
            if(Heights[possPeak-1]<Heights[possPeak]
            and Heights[possPeak+1]
            <Heights[possPeak]):
                runningTotal = runningTotal + 1
        print('Case #' + str(caseNo) + ': ' + str(runningTotal))
        caseNo = caseNo + 1

if __name__ == '__main__':
    main()
