from .openai import open_ai
from .writesonic import writesonic


def models_(data, api, *args, **kwargs):
    if api == 'openai':
        return open_ai(data, *args, **kwargs)
    elif api == 'writesonic':
        writesonic(data, *args, **kwargs)
    else:
        pass
        # raise NotAcceptable();
