import pronouncing
_end = '_end_'

s1= input("Enter string 1:")
p= pronouncing.rhymes(s1)
p.append(s1)

s2= input("Enter string 2:")
q= pronouncing.rhymes(s2)
q.append(s2)

s3= input("Enter string 3:")
r= pronouncing.rhymes(s3)
r.append(s3)

print(p,q,r)
import re
def DAFSA(words):
    num_words = len(words)
    seq_list = []
    for i in range(0,num_words):
        current_word = words[i]
        for j in range(i+1,num_words):
            match_word = words[j]
            search_next = True
            #print("start of our search: \n")
            for curr_char_i in range(0,len(current_word)):
                for match_char_i in range(0,len(match_word)):
                    # search till the matching chars in sequence is found in words
                    if search_next == True:
                        # check if there is a matching character
                        if current_word[curr_char_i] == match_word[match_char_i]:
                            w1 = current_word[curr_char_i:]
                            w2 = match_word[match_char_i:]
                            # also record the unmatched charcter in a sequence
                            u_w1 = current_word[0:curr_char_i]
                            u_w2 = match_word[0:match_char_i]
                            # make sure that the fragment length matches in the sequence of words
                            if len(w1) == len(w2):
                                match_count = 0
                                matched_seq = ""
                                for c1,c2 in zip(w1,w2):
                                    if c1 == c2:
                                        matched_seq = matched_seq + c1
                                        match_count += 1
                                # if the number of match count equals the fragment length
                                if match_count == len(w2):
                                    # when a desired match is found, stop looking further in the match word
                                    search_next = False
                                    word_dict = {}
                                    # handle the right sequences making into the list
                                    if len(u_w1)+len(matched_seq) == len(current_word):
                                            if len(u_w2)+len(matched_seq) == len(match_word):
                                                if len(u_w1) > 0 and len(u_w2) > 0:
                                                    word_dict[u_w1]=matched_seq
                                                    word_dict[u_w2]=matched_seq
                                            # add the matched characters
                                            if len(word_dict)>0:
                                                seq_list.append(word_dict)
                                                break
    print("seq_list--->",seq_list)

print("\n")    
print("---------DAFSA for String 1-----------")
DAFSA(p)
print("\n")
print("---------DAFSA for String 2-----------")
DAFSA(q)
print("\n")
print("---------DAFSA for String 3---------------")
DAFSA(r)

