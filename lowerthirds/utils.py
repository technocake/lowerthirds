import os


def _env(key, default=None, return_type=None, list_element_type=str):
    """
        Function to parse settings from environment consistently.
        Handles parsing of bool/int/list/str values correctly.
        :param key: name of environment variable to load setting from.
        :param default: Optional default value if key is not present in environment.  # noqa
        :param return_type: Optional - specify return_type.
        :param list_element_type: Optional - cast/parse each element of a list with provided callable. Only used if the setting is a list.
        If key is not present in environment, and there is not provided a default value,
        None will be returned.
        Guidelines for settings in Environment
        A couple of conventions exist when designing
        environment variables for settings.
         1. All values are stored as strings in the environment variable
         2. Bools are encoded as one of "1", "True" or "true" if True,
            all other values are interpreted as False
         3. lists are encoded as a string, with the list items
            separated with ","
                in example:  "a,b,c,   d"
            (intentionally put whitespace in there. It is allowed)
        default Values are preffered to be set to the same type as the setting.
        list -> [], str -> '', int -> 0, bool -> True/False etc
    """
    truthy = ["1", "True", "true"]

    if return_type is None:
        # guessing type from default
        return_type = type(default) if default is not None else str

    if return_type is int:
        return int(os.environ.get(key, default))

    elif return_type is bool:
        return str(os.environ.get(key, default)) in truthy

    elif return_type is list:
        if key in os.environ:
            # element_type is used to be called on each element in a list,
            # Used to intepret say a list of ints
            # defaults to str
            data = os.environ.get(key).split(',')
            return [list_element_type(item.strip()) for item in data]
        else:
            # This allows to put a default value of type list.
            # We wont ask for a list encoded as a comma-separated string
            # for default values. But they have to be so in the env var.
            #
            # Warning - if no default is set,
            # it will automatically be set to None.
            return default

    return os.environ.get(key, default)  # default to string