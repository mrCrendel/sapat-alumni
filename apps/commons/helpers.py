import os
import re
import uuid

from django.utils import timezone


def slugify_camelcase(string: str, sep: str = "-") -> str:
    """
    Converts camelcase string to lowercase string divided with given
    separator

    :param string: string to slugify
    :param sep: separator
    :return: slugified string

    With sep='_':
        'CamelCase' -> 'camel_case'
    """
    repl = r"\1{}\2".format(sep)
    s1 = re.sub("(.)([A-Z][a-z]+)", repl, string)
    return re.sub("([a-z0-9])([A-Z])", repl, s1).lower()


def generate_filename(instance, filename: str) -> str:
    """
    Generates a filename for a model's instance

    :param instance: Django model's instance
    :param filename: filename
    :return: generated filename

    Filename consist of slugified model name, current datetime and time
    and uuid
    """
    f, ext = os.path.splitext(filename)
    model_name = slugify_camelcase(instance._meta.model.__name__, "_")
    strftime = timezone.datetime.now().strftime("%Y/%m/%d")
    hex_ = uuid.uuid4().hex
    # return f"{model_name}/{strftime}/{hex_}{ext}"
    return "{}/{}/{}{}".format(model_name, strftime, hex_, ext)
