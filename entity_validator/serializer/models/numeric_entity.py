from entity_validator.serializer.models.base_entity import BaseEntity


class NumericEntity(BaseEntity):
    """
    NumericEntity Model extending common entity attributes from BaseEntity.
    Used in creating a python object with key name's similar to that of json object in case of numeric entity.
    """
    def __init__(self, values, invalid_trigger, key, support_multiple, pick_first, constraint, var_name, **kwargs):
        super().__init__(values, invalid_trigger, key, support_multiple, pick_first)
        self.constraint = constraint
        self.var_name = var_name
