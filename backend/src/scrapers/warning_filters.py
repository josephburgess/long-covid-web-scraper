import warnings
import logging
import re


class CustomFilter(logging.Filter):  # pragma: no cover
    def filter(self, record):
        bert_model_warning = re.search(
            r"Some weights of the model checkpoint at bert-large-uncased were not used",
            record.getMessage(),
        )

        if bert_model_warning:
            return False
        return True


def setup_warnings_and_loggers():  # pragma: no cover
    warnings.simplefilter("ignore", category=FutureWarning)

    logger_transformers = logging.getLogger("transformers.modeling_utils")
    logger_transformers.addFilter(CustomFilter())
