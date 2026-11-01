"""Live integration tests required by the IBM course project."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Validate dominant emotions against the real Watson NLP service."""

    def test_required_examples(self):
        """Check the five required synthetic statements and emotions."""
        examples = (
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        )
        for statement, expected in examples:
            with self.subTest(statement=statement):
                self.assertEqual(
                    emotion_detector(statement)["dominant_emotion"], expected
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
