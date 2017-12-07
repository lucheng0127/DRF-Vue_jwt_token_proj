#-*- coding: utf-8 -*-
import re

def validator_text(value):
    pattern = r"^[\s\S]*[\"#\$%&\'\(\)\*\+/:;<=>?@\[\\\]\^_`\{\|\}~]"
    if re.match(pattern, value):
        return False
    return True
