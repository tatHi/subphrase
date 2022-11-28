from collections import defaultdict

def getFreqBigram(data, maxRepetition, maxLength):
    countDict = defaultdict(lambda:0)
    for line in data:
        for i in range(len(line)-1):
            w = line[i] + ('_',) + line[i+1]
            if countLength(w) <= maxLength and countRepetition(w) <= maxRepetition:
                countDict[w] += 1
    word, freq = sorted(countDict.items(), key=lambda x:x[1])[-1]
    return word, freq

def countLength(word):
    size = len(word[0].split('_') + word[2].split('_'))
    return size

def countRepetition(word):
    maxnum = 1
    num = 1
    line = word[0].split('_') + word[2].split('_')
    for i in range(1, len(line)):
        if line[i]==line[i-1]:
            num += 1
        else:
            if maxnum < num:
                maxnum = num
            num = 1
    if maxnum < num:
        maxnum = num
    return maxnum

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

def countWordSize(data):
    return sum([len(line) for line in data])

def countVocabSize(data):
    return len({w for line in data for w in line})

def merge(data, args):
    mergeList = []
    i = 0
    while True:
        word, freq = getFreqBigram(data, args.maxRepetition, args.maxLength)
        data = updateData(data, word)
        mergeList.append((''.join(word), str(freq)))
        wordSize = countWordSize(data)
        vocabSize = countVocabSize(data)
        i += 1

        print('MERGE:', ''.join(word))
        print('mergeNumber:', i, '(GOAL: %s)'%(str(args.numMerge) if args.numMerge is not None else '-'))
        print('wordSize:', wordSize, '(GOAL: %s)'%(str(args.wordLimit) if args.wordLimit is not None else '-'))
        print('vocSize:', vocabSize, '(GOAL: %s)'%(str(args.vocabLimit) if args.vocabLimit is not None else '-'))
        if args.wordLimit is not None and wordSize <= args.wordLimit:
            break
        if args.vocabLimit is not None and vocabSize >= args.vocabLimit:
            break
        if args.numMerge is not None and i >= args.numMerge:
            break
    return data, mergeList

def save(data, mergeList, args):
    data = [' '.join([w[0] for w in line]) for line in data]
    with open(args.outPath, 'w') as f:
        for line in data:
            f.write(line+'\n')
    with open(args.outPath + '.mergeList', 'w') as f:
        for line in mergeList:
            f.write(' '.join(line)+'\n')

def loadData(args):
    data = [line.strip() for line in open(args.inPath)]
    data = [[(w,) for w in line.split()] for line in data]
    return data

def checkArgs(args, data):
    numWords = countWordSize(data)
    numVocab = countVocabSize(data)

    # only one limit can be accepted?
    print("Merge tokens until ONE OF the following condition would be met:")
    numConditions = 0
    if args.wordLimit is not None:
        print("WORD NUMBER -> %d" % args.wordLimit)
        numConditions += 1
        if args.wordLimit <= numWords:
            print("CAUTION: The specified word limit is already satisfied.")
            print("         Please set a value < current word size (%d)."%numWords)
    if args.vocabLimit is not None:
        print("VOCAB NUMBER -> %d" % args.vocabLimit)
        numConditions += 1
        if numVocab < args.vocabLimit:
            print("CAUTION: The specified vocab limit is already satisfied.")
            print("         Please set a value > current vocab size (%d)."%numVocab)
    if args.numMerge is not None:
        print("MERGE NUMBER -> %d" % args.numMerge)
        numConditions += 1
    if numConditions==0:
        print("You must specify at least one of [--wordLimit, --vocabLimit, --numMerge].")
        exit()

def main(args):
    data = loadData(args)
    checkArgs(args, data)

    data, mergeList = merge(data, args) # conditionをmergeに追記する、vocabをdumpできるようにする
    save(data, mergeList, args) 

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--inPath',default='../data/alice_formatted.txt',type=str)
    parser.add_argument('-o','--outPath',default='../data/result_alice.txt',type=str)
    parser.add_argument('-wl','--wordLimit',default=None, type=int, 
                        help='merge until number of words becomes lower than this limit')
    parser.add_argument('-vl','--vocabLimit',default=None, type=int,
                        help='merge until number of words in *vocab* reaches this limit')
    parser.add_argument('-nm', '--numMerge', default=None, type=int,
                        help='merge numMerge times')
    parser.add_argument('-mr', '--maxRepetition', default=100, type=int,
                        help='maximum number of repetition of the same tokens in merge (when 3, a_a_a_a with 4 repetition is ignored in merging operation)')
    parser.add_argument('-ml', '--maxLength', default=10, type=int,
                        help='maximum number of tokens in a single phrase (when 3, a_b_c_d with 4 tokens in single merge is ignored in meging operation)')
    args = parser.parse_args()

    main(args)
