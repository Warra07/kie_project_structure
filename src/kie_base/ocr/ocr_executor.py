from dataclasses import dataclass
from xml.dom.minidom import Document

from kie_base.schema.config import OcrConfig
from kie_base.schema.data.document import OcrDocument


@dataclass
class OcrExecutor:
    ocr_config: OcrConfig

    def execute_single(self, document: Document) -> OcrDocument:
        """execute ocr on a single document, extract the ocr using azure sdk,
        format the result and initialize the ocr document.

        :param document: the document to process
        :type document: Document
        :return: the document with ocr results
        :rtype: Document
        """
        # TODO execute single ocr step

        return OcrDocument()
