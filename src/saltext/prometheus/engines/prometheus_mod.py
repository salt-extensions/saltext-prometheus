"""
Salt engine module
"""
import logging

log = logging.getLogger(__name__)

__virtualname__ = "prometheus"


def __virtual__():
    # return __virtualname__
    return (False, "The prometheus engine module is not implemented yet")
