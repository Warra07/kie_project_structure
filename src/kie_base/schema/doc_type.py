from enum import Enum
from typing import List
from pydantic import BaseModel, Field


class DocumentLayout(str, Enum):
    standardized_page = "standardized_page"
    standardized_card = "standardized_card"
    nonstandardized = "nonstandardized"


class DocumentField(BaseModel):
    name: str = Field(..., description="the document field name")
    description: str = Field(..., description="the document field description")
    field_type: str = Field(..., description="the document field type")


class DocType(BaseModel):
    name: str = Field(..., description="the document type name")
    description: str = Field(..., description="the document type description")
    document_layout: DocumentLayout = Field(..., description="the document layout")
    fields: List[DocumentField] = Field(..., description="the document fields")
