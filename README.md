Here in this repo we shall discuss about computation of Edit Distance. The dynamic programming table will be populated with cost 
effective value of 1 for insert, 1 for delete , but 2 for substitution. Replacing 2 for substitution of cost is called Levenshtein
minimum edit distance computation. 

For sake of Levenshtein edit distance we just insert the cost computation at line#17 as 2 for substitution and add the cost at line#20. 
Based on these computations, the dp table that we arrive is as we seen on the screen with edit distance equal to 4 on transforming 
sunday to monday having 2 substitutions of "su" to "mo".

<img width="2030" height="1155" alt="image" src="https://github.com/user-attachments/assets/264f88b6-7c0d-47c3-8591-e926cbffd187" />


Let me leave it you to verify the values computed in the table and check yourself. 
