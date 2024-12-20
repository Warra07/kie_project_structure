from kie_base.preprocessing.preprocessing_executor import PreprocesisngExecutor
from kie_base.ocr.ocr_executor import OcrExecutor
from kie_base.classification.classification_executor import CLassificationExecutor
from kie_base.extraction.extraction_executor import ExtractionExecutor
from kie_base.schema.config import OcrConfig, ClassificationConfig, ExtractionConfig
from kie_base.schema.data.document import (
    Document,
    OcrDocument,
    ClassificationDocument,
    ExtractionDocument,
)


def load_ocr_config(document: Document) -> OcrConfig:
    # TODO: Implement the logic to load OCR config based on the document
    return OcrConfig(
        ocr_model="default_model", doc_type_list=[], extract_all_pages=True
    )


def load_classification_config(ocr_document: OcrDocument) -> ClassificationConfig:
    # TODO: Implement the logic to load Classification config based on the OCR document
    return ClassificationConfig(
        classification_model="default_model", doc_type_list=[], use_all_pages=True
    )


def load_extraction_config(
    classification_document: ClassificationDocument,
) -> ExtractionConfig:
    # TODO: Implement the logic to load Extraction config based on the Classification document
    return ExtractionConfig(
        doc_type="default_type", extraction_model="default_model", use_all_pages=True
    )


def single_extraction_pipeline(document_path: str) -> ExtractionDocument:
    # Step 1: Preprocessing
    preprocessing_executor = PreprocesisngExecutor()
    document = preprocessing_executor.execute_single(document_path)

    # Step 2: OCR
    ocr_config = load_ocr_config(document)
    ocr_executor = OcrExecutor(ocr_config)
    ocr_document = ocr_executor.execute_single(document)

    # Step 3: Classification
    classification_config = load_classification_config(ocr_document)
    classification_executor = CLassificationExecutor(classification_config)
    classification_document = classification_executor.execute_single(ocr_document)

    # Step 4: Extraction
    extraction_config = load_extraction_config(classification_document)
    extraction_executor = ExtractionExecutor(extraction_config)
    extraction_document = extraction_executor.execute_single(classification_document)

    return extraction_document


if __name__ == "__main__":
    document_path = "path/to/your/document.pdf"
    extraction_document = single_extraction_pipeline(document_path)
    print(extraction_document)
