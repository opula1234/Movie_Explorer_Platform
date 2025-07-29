from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional, List


class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        from pydantic_core import core_schema

        return core_schema.json_or_python_schema(
            python_schema=core_schema.with_info_plain_validator_function(cls.validate),
            json_schema=core_schema.str_schema(),
        )

    @classmethod
    def validate(cls, value, _info):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)
