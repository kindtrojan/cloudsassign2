# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):

    # input
    input = yield context.call_activity('GetInputDataFn', 'mapreduce')

    # for each tuple, call a Mapper- fan out
    mappers = []
    for pair in input:
        mappers.append(context.call_activity('Mapper', pair))
    # FanIn
    mapper_result = yield context.task_all(mappers)

    # concatenate the results
    mapper_result = sum(mapper_result, [])

    # call the Shuffler
    shuffler_result = yield context.call_activity('Shuffler', mapper_result)

    # for each shuffled tuple, call a Reducer, fan out
    reducers = []
    for pair in shuffler_result:
        reducers.append(context.call_activity('Reducer', pair))
    # wait for all tasks to finish
    output = yield context.task_all(reducers)

    # return the final result
    return output

main = df.Orchestrator.create(orchestrator_function)