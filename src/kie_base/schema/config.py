from typing import List

from pydantic import BaseModel


class OcrConfig(BaseModel):
    ocr_model: str
    doc_type_list: List[str]
