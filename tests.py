import os
import unittest

from xml_analyzer.analyzer import XMLAnalyzer
from xml_analyzer.exceptions import NoMatchesFound


class TestAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.SAMPLES_PATH = os.path.relpath("samples")
        cls.GROUND_TRUTH_PATH = os.path.join(cls.SAMPLES_PATH, "sample-0-origin.html")
        cls.ELEMENT_ID = "make-everything-ok-button"

    def _get_best_match(self, diff_page_path):
        return XMLAnalyzer(
            ground_truth_page_path=self.GROUND_TRUTH_PATH,
            diff_page_path=os.path.join(self.SAMPLES_PATH, diff_page_path),
            element_id=self.ELEMENT_ID
        ).get_best_match_path()

    def test_sample_1(self):
        expected_result = "/html/body/div/div/div[3]/div[1]/div/div[2]/a[2]"
        best_match_path = self._get_best_match("sample-1-evil-gemini.html")
        self.assertEqual(
            best_match_path,
            expected_result
        )

    def test_sample_2(self):
        expected_result = "/html/body/div/div/div[3]/div[1]/div/div[2]/div/a"
        best_match_path = self._get_best_match("sample-2-container-and-clone.html")
        self.assertEqual(
            best_match_path,
            expected_result
        )

    def test_sample_3(self):
        expected_result = "/html/body/div/div/div[3]/div[1]/div/div[3]/a"
        best_match_path = self._get_best_match("sample-3-the-escape.html")
        self.assertEqual(
            best_match_path,
            expected_result
        )

    def test_sample_4(self):
        expected_result = "/html/body/div/div/div[3]/div[1]/div/div[3]/a"
        best_match_path = self._get_best_match("sample-4-the-mash.html")
        self.assertEqual(
            best_match_path,
            expected_result
        )

    def test_sample_5__empty(self):
        self.assertRaises(
            NoMatchesFound,
            self._get_best_match,
            "sample-5-empty.html"
        )


if __name__ == "__main__":
    unittest.main()
