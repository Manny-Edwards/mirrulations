import logging
import os.path
import mirrulations_core.documents_core as dc

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(filename='doc_filter.log', format=FORMAT)
d = { 'clientip': '192.168.0.1', 'user': 'FILTERS'}
logger = logging.getLogger('tcpserver')

PATH = os.getenv("HOME") + "/regulations-data/"


def search_for_document_in_directory(document_id, directory_path=PATH):
    """
    Called by the server to check to see if a document exists in the directory structure
    :param document_id: the document id being searched
    :param directory_path: The directory path being searched in
    :return: Return the full path if the document exists, else return an empty string
    """
    orgs, dock_id, doc_id = dc.get_doc_attributes(document_id)

    full_path = directory_path + orgs + "/" + dock_id + "/" + doc_id
    doc_json = "doc." + doc_id + ".json"

    if os.path.isfile(full_path + "/" + doc_json):
        return full_path
    else:
        return ""
