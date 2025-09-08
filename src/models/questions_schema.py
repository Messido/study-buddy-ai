from typing import List
from pydantic import BaseModel, Field, field_validator


class MCQs(BaseModel):
    question: str = Field(description="the question text")
    options: List[str] = Field(description="list of 4 options")
    correct_answer: str = Field(description="the correct answer from the options")

    @field_validator("question", mode='before')
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get("description", str(v))

        return str(v)



class FillinTheBlanks(BaseModel):
    question: str = Field(description="the question text with '_____' for the blank ")
    answer : str = Field(description="the correct answer to the question ( word or phrase)")
    @field_validator("question", mode='before')
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get("description", str(v))

        return str(v)
