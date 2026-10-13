# AI AGENTS  ==> COMBINATION OF LLM AND FUNCTIONS/API ACCESS(tools)

## How llm knows which tool is avialable

--> Example:
1. give me answer of of 10*21
2. which is shubham kumar?
-> these are two query aske to llm , here how llm wil choose between calculator and websearch for better answer for these two query

## Important steps
1. Create function: whatever we will wants from our agents.
2. Available tools: the tool(api) will used by llm respective of query.
3. Tool[]: type:function, name:web_search , description : when to use(search the web for current information)
4. Parameter: query:string , description:string consice web search query
5. Agent Instruction: give instruction in sys_prompt

google search api : tavily