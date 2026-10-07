# RAG Evaluation : this evaluate/tests how our RAG are working
--> suppose ask a question to RAG, then how can we determine the answer is correct or not.here we use evaluation to determine the answer is correct or not.

## architecture of RAG
==> knowledge base --> Embedding --> vectors --> vectorDB --> QUERY --> vectorsDB --> context --> LLM --> Answer


==> reason behind RAG failure:

1. wrong knowledge base
2. issue in vector's simlarity -> result in wrong context.
3. issue with LLM to read and understand.


## Evaluation process:
1. create a golden dataset for evaluation (similar to testcases in leetcode) {conatains question , ground truth }-> based on knowledgebase

2. layer by layer checking: (query -> qdrant{top3 vectors})
=> According to question, correct context is comming or not.
   1. check precision/accuracy : suppose we aske a question to RAG, it extract context (top3 vectors line) from qdrant(vectordb) but there is only 2 lines relevant to question --> its precision will be 2/3*100 = 66%
   2. check recall : suppose from above 2 relevant line , only one is retrived --> its recall is 1/2*100 = 50%

NOTE: if precision and recall both are high then, there is problem with LLM

3. Issue with LLM:
	1. faithfulness: suppose there is context containing , 12 days of paid leave but LLM answers 10 days of leave, here its shows LLM is hallucinating (not faithfull )

	2. correctness: suppose there is 10 days of paid leave in company but the context contain 10 days of paid leave and LLM also answer 10 days of leave ( here llm is faithfull)

	3. relevency: suppose there is context (promotion will be in november) , but LLM answers definition of promotions.

	  

NOTE 1 : there is high chance of LLM to be incorrect and faithfull at the same time OR correct and unfaithfull at the same time ( it means its hallucinating)

NOTE 2 : if we getting low precision , reduce the value of k in topk vector line OR set a threshold (similar, score > 0.5) |  if we are getting low recall , increase the value of topk or increase the threshold value(similar, score >0.9)

NOTE 3 : if answer is not faithfull , have focus on system prompts (donot hallucinate) | if answer is incorrect , the have to focus on context/knowledge (check precision or recall) | if answer is not relevence , correct system prompt ( answer to the point)