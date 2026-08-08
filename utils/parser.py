import json
import re
import logging

logger = logging.getLogger("Parser")


def extract_json(text: str):
    """
    Extract JSON from an LLM response.

    Handles:
    - ```json ... ```
    - raw JSON
    - extra explanation before/after JSON

    Returns:
        dict
    """

    if not text:
        return {}

    text = text.strip()

    # ----------------------------------------
    # Remove markdown fences
    # ----------------------------------------

    text = re.sub(r"^```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    text = text.strip()

    # ----------------------------------------
    # Try direct parsing
    # ----------------------------------------

    try:
        return json.loads(text)

    except Exception:
        pass

    # ----------------------------------------
    # Extract first JSON object
    # ----------------------------------------

    match = re.search(
        r"\{.*\}",
        text,
        flags=re.DOTALL,
    )

    if match:

        candidate = match.group(0)

        try:

            return json.loads(candidate)

        except Exception:

            logger.warning(
                "Failed parsing extracted JSON."
            )

    # ----------------------------------------
    # Final fallback
    # ----------------------------------------

    logger.warning("\n========== RAW MODEL OUTPUT ==========\n")
    logger.warning(text)
    logger.warning("\n======================================\n")

    return {
        "raw_response": text,
        "parsing_error": True,
    }