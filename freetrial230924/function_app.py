import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get the 'name' and 'pronoun' from the query string or the request body
    name = req.params.get('name')
    pronoun = req.params.get('pronoun')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            pronoun = req_body.get('pronoun')

    if name and pronoun:
        return func.HttpResponse(
            f"Hello {name}, nice to know that your pronoun is this {pronoun}.",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please provide both a name and a pronoun.",
            status_code=400
        )
