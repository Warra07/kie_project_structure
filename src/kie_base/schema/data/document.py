from pydantic import BaseModel


class Document(BaseModel):
    document_id: str
