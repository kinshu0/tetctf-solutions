
# TetCTF 2023 Writeups

Braindump / Writeups for challenges I've solved and will potentially add more solutions

## Challenges

### newyearbot

From the code we can see that `eval` is called on the option parameter form POST input on the request. The greetType can be set to the `FL4G` variable that stores the flag. The number, however, is filtered through the `botValidator` function. Only certain operators are allowed and the eval expression's index `FL4G[whatever_idx]` cannot have more than one number and any character. The operators that are allowed are `-` and `~` which are the negative and bitwise not operator.
So, using the short little script gen_inputs.py, I generate various positive and negative expressions for the index: `['0', '1', '2', '3', '4', '5', '-~5', '-~-~5', '-~-~-~5', '-~-~-~-~5', '-~-~-~-~-~5', '-~-~-~-~-~-~5', '-~-~-~-~-~-~-~5', '~-~-~-~-~-~-~5', '~-~-~-~-~-~5', '~-~-~-~-~5', '~-~-~-~5', '~-~-~5', '~-~5', '~5', '-5', '-4', '-3', '-2', '-1', ]` that iterates over all of the characters in the flag.
This is then sent as a POST request using sol.py and each character of the flag is put together.