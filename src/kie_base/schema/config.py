from typing import List
from xml.dom.minidom import DocumentType

from pydantic import BaseModel


class OcrConfig(BaseModel):
    ocr_model: str
    doc_type_list: List[DocumentType]
    extract_all_pages: bool = True
    pages_to_extract: List[int] = []


class ClassificationConfig(BaseModel):
    classification_model: str
    doc_type_list: List[DocumentType]
    use_all_pages: bool = True
    pages_to_use: List[int] = []
    include_tables: bool = True
    include_figures: bool = False


class ExtractionConfig(BaseModel):
    doc_type: DocumentType
    extraction_model: str
    use_all_pages: bool = True
    include_tables: bool = True
    include_figures: bool = False
