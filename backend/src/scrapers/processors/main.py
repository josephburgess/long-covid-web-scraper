from .data_processor import main as data_processor_main
from .top_words_extractor import main as top_words_extractor_main


def run_processors():
    print("Running processors...")
    data_processor_main()
    top_words_extractor_main()


if __name__ == "__main__":
    run_processors()
