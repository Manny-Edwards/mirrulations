import json
import logging
import os

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(filename='client.log', format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'CONFIG'}
logger = logging.getLogger('tcpserver')


def read_value(value):
    """
    Reads a file from the configuration JSON file.
    :param value: Value to be read from the JSON
    :return: Value read from the JSON
    """
    logger.debug('Calling Function: %s', 'read_value: Reading a value from the configuration file', extra=d)
    logger.info('Reading config file...')
    try:
        logger.debug("Assign Variable: %s", 'read_value: loading json from config', extra=d)
        configurationpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../config.json")
        contents = json.loads(open(configurationpath, "r").read())
        logger.debug("Variable Success: %s", 'read_value: found json from config', extra=d)
        logger.info('Config file read successful...')
        result = contents[value]
    except FileNotFoundError:
        logger.debug('Exception: %s', 'read_value: Error finding JSON', extra=d)
        logger.error('File Not Found Error')
        return None
    except IOError:
        logger.debug('Exception: %s', 'read_value: Error opening JSON', extra=d)
        logger.error('Input/Output Error')
        return None
    except json.JSONDecodeError:
        logger.debug('Exception: %s', 'read_value: Error loading JSON', extra=d)
        logger.error('JSON Decode Error')
        return None
    except KeyError:
        logger.debug('Exception: %s', 'config: Caught KeyError, no value present for: ' + str(value) +
                     '. Returning None.', extra=d)
        logger.error('Key Error')
        return None
    else:
        return result
