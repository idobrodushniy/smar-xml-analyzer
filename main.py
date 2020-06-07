import logging
import sys

from xml_analyzer.analyzer import XMLAnalyzer
from xml_analyzer.exceptions import NoMatchesFound

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(levelname)s %(message)s',
)
logger = logging.getLogger("main")

if __name__ == "__main__":
    ground_truth_page_path, diff_page_path, element_id = sys.argv[1:]
    analyzer = XMLAnalyzer(
        ground_truth_page_path=ground_truth_page_path,
        diff_page_path=diff_page_path,
        element_id=element_id
    )
    try:
        best_match_path = analyzer.get_best_match_path()
        logger.info(f"The best match path -> {best_match_path}")
    except NoMatchesFound as e:
        logger.error(e)
    except KeyError:
        logger.error(f"Element with id `{element_id}` doesn't exist in {ground_truth_page_path}.")
