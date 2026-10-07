from langchain_text_splitters import (
	CharacterTextSplitter, RecursiveCharacterTextSplitter
)

text = """ The Taj Mahal is a stunning white marble mausoleum located on the southern bank of the Yamuna River in Agra, India. 
Commissioned in 1632 by the Mughal Emperor Shah Jahan to house the tomb of his beloved wife, Mumtaz Mahal, this UNESCO World 
Heritage Site stands as a universal symbol of eternal love and a masterpiece of Indo-Islamic architecture. The complex features 
a symmetrical design with a large central onion dome, four soaring corner minarets, and exquisite pietra dura inlay work using 
precious and semi-precious stones. Surrounded by a formal charbagh garden with a long reflecting pool, the monument famously 
changes its hue throughout the day, glowing pink in the morning light, milky white in the evening, and golden under the moonlight.
"""

# 1. FIXED-SIZED CHUNKING

fixed = CharacterTextSplitter(
	separator="",
	chunk_size=100,
	chunk_overlap=0
)

print("\==========FIXED SIZE========")

for i, chunk in enumerate(fixed.split_text(text),1):
	print(f"\nChunk {i}:")
	print(chunk)
	print("==============")

# 2. PARAGRAPH CHUNKING

paragraph = CharacterTextSplitter(
	separator="\n\n",
	chunk_size=100,
	chunk_overlap=0
)

print("\n=========PARAGRAPH=======")

for i, chunk in enumerate(paragraph.split_text(text),1):
	print(f"\nChunk {i}:")
	print(chunk)
	print("==============")

# 3. RECURSIVE CHUNKING

recursive = RecursiveCharacterTextSplitter(	
	chunk_size=100,
	chunk_overlap=20
)

print("\n=========RECURSIVE=======")

for i, chunk in enumerate(recursive.split_text(text),1):
	print(f"\nChunk {i}:")
	print(chunk)
	print("==============")


