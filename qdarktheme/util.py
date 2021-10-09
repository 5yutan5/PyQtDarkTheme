from __future__ import annotations

import logging
import re


# https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729
def multireplace(target: str, replacements: dict[str, str]) -> str:
    if len(replacements) == 0:
        return target

    replacements_sorted = sorted(replacements, key=len, reverse=True)
    replacements_escaped = [re.escape(i) for i in replacements_sorted]
    pattern = re.compile("|".join(replacements_escaped))
    return pattern.sub(lambda match: replacements[match.group()], target)


def create_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("[%(name)s] [%(levelname)s] %(message)s"))
    logger.addHandler(ch)
    return logger
