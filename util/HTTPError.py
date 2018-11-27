'''
Created on 28-Nov-2018

@author: tanumoy
'''
import falcon

class HTTPError(falcon.HTTPError):
    """
    HTTPError that stores a dictionary of validation error messages.
    """

    def __init__(self, status, errors=None, *args, **kwargs):
        self.errors = errors
        super().__init__(status, *args, **kwargs)

    def to_dict(self, *args, **kwargs):
        """
        Override `falcon.HTTPError` to include error messages in responses.
        """

        ret = super().to_dict(*args, **kwargs)

        if self.errors is not None:
            ret['errors'] = self.errors

        return ret