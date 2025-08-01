import re
from pydantic import BaseModel, Field, field_validator


class DateTimeModel(BaseModel):
    date: str = Field(description="Properly formatted date", pattern='^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$')

    @field_validator("date")
    def check_format_date(cls, v):
        if not re.match(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$', v):
            raise ValueError("The date should be in format 'DD-MM-YYYY HH:MM'")
        return v

class DateModel(BaseModel):
    date: str = Field(description="Properly formatted date", pattern='^\d{2}-\d{2}-\d{4}$')

    @field_validator("date")
    def check_format_date(cls, v):
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', v):
            raise ValueError("The date should be in format 'DD-MM-YYYY'")
        return v

class IdentificationTickerNumberModel(BaseModel):
    id: str = Field(description="Identification Number (7 or 8 digits long)")

    @field_validator("id")
    def check_format_id(cls, v):
        if not re.match(r'^\d{7,8}$', str(v)):
            raise ValueError("The ID number should be a 7 or 8 digit number")
        return v


class ToolsdataModel(BaseModel):
    query: str = Field(description="it should be user query with meaningful to give answer")