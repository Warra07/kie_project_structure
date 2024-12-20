from typing import Self
from xml.dom.minidom import Document


class PreprocesisngExecutor:

    def execute_single(self: Self, path: str) -> Document:
        """validate extension, extract metadata and initialize ocr config for a single pdf

        :param path: path of the pdf
        :type path: str
        :return: the basic ocr config and relevant document information
        :rtype: Tuple[Document, OcrConfig]
        """
        # TODO execute single preprocessing step

        return Document()
