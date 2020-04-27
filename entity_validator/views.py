from entity_validator.serializer.schemas.finite_set_entity_schema import FiniteSetEntitySchema
from entity_validator.serializer.schemas.numeric_entity_schema import NumericEntitySchema
from entity_validator.validator_service.validator import EntityValidator
from entity_validator.constants.constants import Constants as c
from marshmallow import INCLUDE, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class FiniteValues(APIView):
    def post(self, request):
        """
        Post API to validate an entity with a finite set of values.
        :param request: request made on the webpage.
        :return: Response with either Error message and HTTP status 400 if bad request else a dictionary as follows -
                    {
                        "filled": <filled flag>,
                        "partially_filled": <partially filled flag>,
                        "trigger": <trigger value>,
                        "parameters": <params dict from func>
                    }
﻿        """
        schema = FiniteSetEntitySchema()
        try:
            entity_obj = schema.load(request.data, unknown=INCLUDE)
        except ValidationError as e:
            return Response(data=e.messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            validator = EntityValidator()
            res = validator.validate_finite_values_entity(**vars(entity_obj))
            return Response(
                {c.staticFilled: res[0], c.staticPartial: res[1], c.staticTrigger: res[2], c.staticParams: res[3]})


class NumericConstraints(APIView):
    def post(self, request):
        """
        POST API to validate an entity with a numeric value extracted and constraints on the value extracted.
        :param request: request made on the webpage.
        :return: Response with either Error message and HTTP status 400 if bad request else a dictionary as follows -
                    {
                        "filled": <filled flag>,
                        "partially_filled": <partially filled flag>,
                        "trigger": <trigger value>,
                        "parameters": <params dict from func>
                    }
        """
        schema = NumericEntitySchema()
        try:
            entity_obj = schema.load(request.data, unknown=INCLUDE)
        except ValidationError as e:
            return Response(data=e.messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            validator = EntityValidator()
            res = validator.validate_numeric_constraints_entity(**vars(entity_obj))
            return Response(
                {c.staticFilled: res[0], c.staticPartial: res[1], c.staticTrigger: res[2], c.staticParams: res[3]})
