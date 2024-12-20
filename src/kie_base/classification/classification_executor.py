from dataclasses import dataclass
from kie_base.schema.config import ClassificationConfig
from kie_base.schema.data.document import ClassificationDocument, OcrDocument


@dataclass
class CLassificationExecutor:
    classification_config: ClassificationConfig

    def execute_single(self, document: OcrDocument) -> ClassificationDocument:
        """execute classification on a single document, extract the classification
          using azure openai sdk,
        format the result and initialize the classification document.

        :param document: the document to process
        :type document: OcrDocument
        :return: the document with classification results
        :rtype: Document
        """
        # TODO execute single classification step
        """
            experimenté le fait de faire une première classification plus simple en utilisant
            uniquement la première page du document pour vérifier la classification sab,
            si ce n'est pas suffisant
            on peut ensuite utiliser le reste des pages pour une classification plus fine
            - load du modèle approprié
            - définition du system role
            - formatage du prompt avec les doc type et descriptions
            - ajout du context: formatage (markdown) en prenant en compte le parametrage
            - (eventuellement) chunking
            si nécessaire
            - aggrégation du resultat de sortie
        """

        return ClassificationDocument()
