import logging
from typing import List

from lxml import html

from .exceptions import NoMatchesFound

logger = logging.getLogger(__name__)


class XMLAnalyzer:
    def __init__(self, ground_truth_page_path: str, diff_page_path: str, element_id: str):
        self.ground_truth_data = self._parse_xml(ground_truth_page_path)
        self.diff_page_data = self._parse_xml(diff_page_path)

        self.element_id = element_id

    def get_best_match_path(self) -> str:
        ground_element = self.ground_truth_data.get_element_by_id(self.element_id)
        diff_elements = self.diff_page_data.cssselect(ground_element.tag)
        ground_element_attributes = ground_element.items()
        ground_element_text = ground_element.text.strip()

        max_matches_count = 0
        best_match = None

        for el in diff_elements:
            matches_count = self._match_element_with_ground_truth(
                ground_element_attributes,
                ground_element_text,
                el
            )
            if matches_count > max_matches_count:
                max_matches_count = matches_count
                best_match = el

        if best_match is None:
            raise NoMatchesFound("No suitable matches were found.")
        logger.debug(
            f"Element {best_match.tag} {best_match} was considered to be the best match"
            f" because of matching by {max_matches_count} criteria."
        )
        return self.diff_page_data.getroottree().getpath(best_match)

    def _parse_xml(self, file_path: str) -> html.HtmlElement:
        return html.parse(file_path).getroot()

    def _match_element_with_ground_truth(
            self,
            ground_element_items: List[html.HtmlElement],
            ground_element_text: str,
            diff_element: html.HtmlElement
    ) -> int:
        matches = 0

        for key, value in ground_element_items:
            if value == diff_element.get(key):
                matches += 1

        if ground_element_text == diff_element.text:
            matches += 1

        return matches
