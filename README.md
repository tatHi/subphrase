# subphrase
bpe for words
  
## usage
```
$ python bpe.py -i ../data/alice_formatted.txt -o ../data/alice_formatted.txt.tokenized -nm 500
```

Options:
```
$ python bpe.py -h
usage: bpe.py [-h] [-i INPATH] [-o OUTPATH] [-wl WORDLIMIT] [-vl VOCABLIMIT] [-nm NUMMERGE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPATH, --inPath INPATH
  -o OUTPATH, --outPath OUTPATH
  -wl WORDLIMIT, --wordLimit WORDLIMIT
                        merge until number of words becomes lower than this limit
  -vl VOCABLIMIT, --vocabLimit VOCABLIMIT
                        merge until number of words in *vocab* reaches this limit
  -nm NUMMERGE, --numMerge NUMMERGE
                        merge numMerge times
```
  
Words in input data must be segmented by ' '.  
Marged words are combined with '\_' as phrase.

