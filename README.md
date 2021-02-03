# Deterministic Acyclic Finite State Automaton(DAFSA)

In my implementation, I have used the concept of DAFSA to find out the characters that are responsible for rhyming from the list of rhyming words.
For this, I have used "pronouncing" inbuilt python library that generates the list of rhyming words from the user input word.
After the list of rhyming words are generated, I passed it through my self made DAFSA function.

The DAFSA function checks the list by taking a pair of all possible combinations. The pairs are checked in left to right sequence. 

The pair of rhyming words are then stored in the list which is of dictionary format. Were key represents the sequence of characters not responsible for rhyming and value represents the sequence of characters responsible for rhyming.


