# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

def main(pair):
    # input -(word, list of 1s)
    # output - (word, sum of 1s)

    out = (pair[0], len(pair[1]))
    return out
