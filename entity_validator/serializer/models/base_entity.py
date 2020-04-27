class BaseEntity:
    """
    Class representing attributes common to both entity models used to deserialize the json object into python object in
     order to achieve object-oriented programming.
    Will function as a base class for both entity model classes.
    """

    def __init__(self, values, invalid_trigger, key, support_multiple, pick_first):
        self.values = values
        self.invalid_trigger = invalid_trigger
        self.key = key
        self.support_multiple = support_multiple
        self.pick_first = pick_first
