# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt


def main(linepair) -> list:
    # input is a tuple of linenumber and content

    line = linepair[1]

    words = line.lower().split()
    outlist = list(zip(words,[1]*len(line)))
    return outlist
