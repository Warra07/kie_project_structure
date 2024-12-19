from typing import Self, Tuple
from xml.dom.minidom import Document

from kie_base.schema.config import OcrConfig


class Preprocesisng:

    def execute_single(self: Self, path: str) -> Tuple[Document, OcrConfig]:
        # TODO execute single
        """

        - Validation des extensions
        - extraction de metadata relatif au document
        - initialisation de la configuration de l'ocr

        """

        return Document(), OcrConfig()
