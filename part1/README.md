## WHY CHUNKING MATTERS MORE THAN YOU THINK:

Every senior RAG engineer will tell you the same thing - you spend more time tuning chunking than any other RAG component. Get chunking right and mediocre retrieval works fine. Get chunking wrong and no amount of advanced retrieval, reranking, or better embeddings will save you. Most tutorials skip this entirely or reduce it to "split every 500 characters" - which is exactly why so many production RAG systems return wrong answers.

## WHAT YOU WILL LEARN IN THIS EPISODE:

Why chunking is the #1 hidden cause of bad RAG systems
4 chunking strategies compared live on the same document
Fixed-size splitting - why it's terrible and when it might still work
Paragraph-based splitting - the intuitive but flawed middle ground
Recursive character splitting - the workhorse used in 80% of production RAG
Markdown-aware splitting - the best choice for docs, wikis, and tutorials
The chunk size + overlap decision framework
Why you should always think in tokens, not characters
The chunking strategy decision tree by content type (prose, docs, code, transcripts)

## WHAT WE BUILD IN THIS PART:

Two Python scripts that make chunking trade-offs immediately visible:
1. Chunking Strategies Comparison - see the same text split 4 different ways, watch code blocks get mangled by naive splitters
2. Chunk Size Tuning - see how the same text produces wildly different chunks based on size and overlap settings

## INTERVIEW QUESTIONS THIS PART PREPARES YOU FOR:

What chunking strategies are there and when do you use each?
What is chunk overlap and why does it matter?
How do you decide chunk size?
What is parent-child chunking?
Why does chunking impact retrieval quality?
Chunk size in tokens or characters?

If you can answer these clearly after this episode, you are ahead of most AI Engineer candidates in the market.

## THE KEY MENTAL MODEL:

Chunking is like cutting a big dosa before serving. Cut too small and it's not filling. Cut too big and it's hard to eat. Cut across the middle and it becomes messy. There is a right way based on what the eater will do with it. Same with LLMs eating chunks - the right chunking strategy depends entirely on your content type and query patterns.

THE PRODUCTION DEFAULT:

For most RAG projects, start with RecursiveCharacterTextSplitter at 500 tokens (approximately 2000 characters) with 50 token overlap. Ship it. Measure with evaluation. Tune from there. Do not over-optimize chunking upfront - real teams iterate based on eval data, they do not guess the perfect number.


# Overview

## chunking: chunking is a menthod of spliting kowledge into chunk, like DSA problem which algorithm will used when, chunking is used according to required problem.

==> suppose we have 6 line of knowledgebase, we usually conver each line as a chunk/vector but real documents are not like that(million line of document cannot converted as vector line by line). if we have to create rag of book (1000 pages), then it is very obious to create array/chunks according to our need. not line by line

## stratigies  for chunking
1. Fixed size chunking : if we have to create a rag of a book (100 pages), then we will create every 50 word as chunks.
--> problem: very strict type of chunking.
Example: suppose any line is of 60 words, but we have applied fixed sized chunking of 50 then it will cut the sentence which result in lost of meaning of sentence. and when we applied chunk size of 500 , it will contain too many concept in it.

2. Separator / paragraph based chunking : we will create each paragraph as new chunk.
--> in a book if one paragraph contains 20 lines and other contain 2000 line , there will be problem occur to understand the meaning for RAG. (too small/too big)

3. Recursive chunking : in this chunk also paragraph is used as separator but we will use different separator for further chunking process (like endline, full stop, comma, colon etc)
Example: firstly we will take a paragraph and check is this too big if yes then find next separator like endline, repeat this process util find best chunk according.


NOTE : Overlap in recursive

Example: shubham came from college and went to market.
chunk1: shubham came from college and
chunk2: college and went to market
chunk3: went to market
 
=> if recursive break some meaning, overlap solve that.

4. semantic : Break chunk on the basis of meaning.
Example: text-> we launch a new iphone 18 today, it has 200 mp camera. Apple's revenue went up by 18%.
chunk1: we launch a new iphone 18 today, it has 200 mp camera.
chunk2: Apple's revenue went up by 18%.

NOTE: we will decide which chunking stratiegies is best for our RAG.