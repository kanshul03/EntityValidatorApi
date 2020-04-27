from entity_validator.serializer.models.base_entity import BaseEntity


class FiniteSetEntity(BaseEntity):
    """
    FiniteSetEntity Model extending common entity attributes from BaseEntity.
    Used in creating a python object with key name's similar to that of json object in case of finite set entity.
    """

    def __init__(self, values, supported_values, invalid_trigger, key, support_multiple, pick_first, **kwargs):
        super().__init__(values, invalid_trigger, key, support_multiple, pick_first)
        self.supported_values = supported_values
