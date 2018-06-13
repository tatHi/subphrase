# subphrase
bpe for words
  
## usage
```
$ python bpe.py -i ../data/alice_formatted.txt -o ../data/result_alice.txt -l 25000
```
  
-i, --inPath: input data path  
-o, --outPath: output result path  
-l, --limit: word size limitation  
  
Words in input data must be segmented by ' '.  
Marged words are combined with '\_' as phrase.

