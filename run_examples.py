"""Display the required packaging and formatting examples from the course."""

from EmotionDetection import emotion_detector

for statement in (
    "I am so happy I am doing this",
    "I hate working long hours",
    "",
):
    print(repr(statement), emotion_detector(statement))
