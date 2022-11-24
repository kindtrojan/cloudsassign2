# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from collections import defaultdict

def main(pairs) -> list:
    # input is the output of ALL mappers, that is a list of pairs (word, 1)
    # output is the input of ALL reducer, that is a list of pairs (word, list of 1s)

    out = defaultdict(list)

    for k, v in pairs:
        out[k].append(v)

    return list(out.items())
