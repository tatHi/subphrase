# subphrase
bpe for words
  
## usage
```
$ python bpe.py --inPath ../data/alice_formatted.txt --outPath ../data/alice_formatted.txt.tokenized -nm 500 --maxLength 10 --maxRepetition 3
```

Options:
```
$ python bpe.py -h
usage: bpe.py [-h] [-i INPATH] [-o OUTPATH] [-wl WORDLIMIT] [-vl VOCABLIMIT] [-nm NUMMERGE] [-mr MAXREPETITION] [-ml MAXLENGTH]

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
  -mr MAXREPETITION, --maxRepetition MAXREPETITION
                        maximum number of repetition of the same tokens in merge (when 3, a_a_a_a with 4 repetition is ignored in merging operation)
  -ml MAXLENGTH, --maxLength MAXLENGTH
                        maximum number of tokens in a single phrase (when 3, a_b_c_d with 4 tokens in single merge is ignored in meging operation)
```
  
Words in input data must be segmented by ' '.  
Marged words are combined with '\_' as phrase.

