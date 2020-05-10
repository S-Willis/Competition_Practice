testCases = int(input())

Ns = [None]*testCases
Ds = [None]*testCases
Xss = [None]*testCases

for case in range(testCases):
    nAndD = input()
    Ns[case] = int(nAndD.split()[0])
    Ds[case] = int(nAndD.split()[1])
    Xss[case] = [int(s) for s in input().split(" ")]

for case in range(testCases):
    N = Ns[case]
    D = Ds[case]
    Xs = Xss[case]

    runningAns = D
    Xs.reverse()

    for X in range(N):
        while(runningAns%Xs[X]!=0):
            runningAns = runningAns - 1

    print('Case #' + str(case+1) + ': ' + str(runningAns))
