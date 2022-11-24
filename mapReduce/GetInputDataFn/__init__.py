# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt


import os
from azure.storage.blob import BlobServiceClient


def main(containername: str) -> list:

   
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=mapreducedurable;AccountKey=DERmVGNMeHj8UcWjcpBWiSu0g8MYLTI4q9uxUk6iU2DcIMOEd+BQ0F8zNmcW8Ls+1CI4UJ7J6ldD+AStLmopEw==;EndpointSuffix=core.windows.net")

    
    container_client = blob_service_client.get_container_client(container=containername)

    # list the blobs in the container
    blob_list = container_client.list_blobs()

    print(blob_list)
    line_pairs = []

    for blob in blob_list:
        file = container_client.download_blob(blob.name).content_as_text()
        lines = file.splitlines()
        line_numbers = list(range(1, len(lines)+1))
        line_pairs = line_pairs + list(zip(line_numbers, lines))


    return line_pairs
