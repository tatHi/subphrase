from collections import defaultdict

def getFreqBigram(data):
    countDict = defaultdict(lambda:0)

    for line in data:
        for i in range(len(line)-1):
            w = line[i] + ('_',) + line[i+1]
            countDict[w] += 1
    k,v = sorted(countDict.items(), key=lambda x:x[1])[-1]
    return k

def updateData(data, x):
    neoData = []
    for line in data:
        neoLine = []
        i = 0
        while i < len(line)-1:
            w = line[i]+('_',)+line[i+1]
            if w==x:
                w = (line[i][0]+'_'+line[i+1][0],)
                neoLine.append(w)
                i+=2
            else:
                neoLine.append(line[i])
                i+=1
        if i<len(line):
            neoLine.append(line[-1])
        neoData.append(neoLine)
    return neoData

def main(inPath, outPath, limit):
    data = [line.strip() for line in open(inPath)]
    data = [[(w,) for w in line.split()] for line in data]

    while True:
        w = getFreqBigram(data)
        data = updateData(data,w)
        wordSize = sum([len(line) for line in data])
        vocSize = len({w for line in data for w in line})
        print('wordSize:', wordSize, w)
        print('vocSize:', vocSize)
        if wordSize<limit:
            break

    data = [' '.join([w[0] for w in line]) for line in data]
    f = open(outPath, 'w')
    for line in data:
        f.write(line+'\n')
    f.close()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--inPath',default='../data/alice_formatted.txt',type=str)
    parser.add_argument('-o','--outPath',default='../data/result_alice.txt',type=str)
    parser.add_argument('-l','--limit',default=25000,type=int)
    args = parser.parse_args()
    main(args.inPath, args.outPath, args.limit)
