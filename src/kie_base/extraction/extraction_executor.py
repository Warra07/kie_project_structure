from dataclasses import dataclass

from kie_base.schema.config import ExtractionConfig
from kie_base.schema.data.document import ClassificationDocument, ExtractionDocument


@dataclass
class ExtractionExecutor:
    extraction_config: ExtractionConfig

    def execute_single(self, document: ClassificationDocument) -> ExtractionDocument:
        """execute extraction on a single document, extract the extraction using azure openai sdk,
        format the result and initialize the extraction document.

        :param document: the document to process
        :type document: ClassificationDocument
        :return: the document with extraction results
        :rtype: Document
        """
        # TODO execute single extraction step

        """Extraction

        - load du modèle approprié
        - cas genAI:
            - définition du system role
            - formatage du prompt avec le doc type, le champ (field) et leurs descriptions
            - ajout du context: formatage (markdown) en prenant en compte le parametrage
            - (eventuellement) chunking
        si nécessaire
            - aggrégation du resultat de sortie

        - cas prebuilt model:
            - extraction des champs
            - formatage
        
        - si signature (ou autre objet): traitement
        spécifique pour détécter la présence de l'objet.
        """

        return ExtractionDocument()
