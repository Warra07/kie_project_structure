from typing import Any, Dict, List
from xml.dom.minidom import DocumentType
from pydantic import BaseModel

from kie_base.schema.config import ClassificationConfig, ExtractionConfig, OcrConfig


class Document(BaseModel):
    document_id: str
    document_full_path: str
    client_id: str
    nb_pages: int
    sab_category: str
    sab_code: str
    rubrique_ged: str
    doc_type_reference: str


class OcrDocument(BaseModel):
    document: Document
    ocr_config: OcrConfig
    ocr_results: Dict[str, Any]  # TODO: define ocr results schema


class ClassificationDocument(BaseModel):
    ocr_document: OcrDocument
    classification_config: ClassificationConfig
    formatted_classification_context: str
    predicted_document_type: DocumentType
    predicted_document_type_confidence: float


class DocumentField(BaseModel):
    field_name: str  # TODO: define field name enum
    field_type: str  # TODO: define field type enum
    field_value: str
    field_confidence: float


class DocumentPrediction(BaseModel):
    doc_type: DocumentType
    document_extraction_confidence: float
    fields: List[DocumentField]


class ExtractionDocument(BaseModel):
    classification_document: ClassificationDocument
    extraction_config: ExtractionConfig
    formatted_extraction_context: str
    global_confidence: float
    documents: List[DocumentPrediction]
