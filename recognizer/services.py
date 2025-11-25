"""PaddlePaddle-based formula recognizer with a graceful fallback."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from django.conf import settings

logger = logging.getLogger(__name__)


@dataclass
class RecognitionResult:
    latex: str
    python_expression: str
    confidence: float


class PaddleFormulaRecognizer:
    def __init__(self) -> None:
        self._ocr = None
        if settings.USE_DUMMY_RECOGNIZER:
            logger.warning("Using dummy recognizer; set USE_DUMMY_RECOGNIZER=false to enable PaddleOCR if installed.")
            return
        try:
            from paddleocr import PaddleOCR

            self._ocr = PaddleOCR(use_angle_cls=True, lang="en")
            logger.info("PaddleOCR initialized for formula recognition.")
        except Exception as exc:  # pragma: no cover - runtime dependency
            logger.warning("Falling back to dummy recognizer: %s", exc)
            self._ocr = None

    def predict(self, image_path: Path) -> RecognitionResult:
        if self._ocr is None:
            return self._dummy_result()

        # Note: PaddleOCR is used as a lightweight text detector here. In a production
        # setup you can swap in Paddle's dedicated math formula recognizer for richer
        # LaTeX output. The below keeps the example offline-friendly.
        ocr_result = self._ocr.ocr(str(image_path), cls=True)
        flattened = " ".join(line[1][0] for page in ocr_result for line in page)
        latex = flattened if flattened else "\\text{(未识别到内容)}"
        python_expr = f"sympy.sympify('{flattened}')" if flattened else "# 无可用表达式"
        confidence_scores = [line[1][1] for page in ocr_result for line in page]
        confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0.0
        return RecognitionResult(latex=latex, python_expression=python_expr, confidence=confidence)

    @staticmethod
    def _dummy_result() -> RecognitionResult:
        return RecognitionResult(
            latex=r"E = mc^2",
            python_expression="E = m * c**2",
            confidence=0.0,
        )


def get_recognizer() -> PaddleFormulaRecognizer:
    # Memoization is intentionally simple to keep the codebase lightweight.
    if not hasattr(get_recognizer, "_instance"):
        get_recognizer._instance = PaddleFormulaRecognizer()  # type: ignore[attr-defined]
    return get_recognizer._instance  # type: ignore[attr-defined]
