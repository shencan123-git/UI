#!/usr/bin/
# -*- coding: UTF-8 -*-

from enum import Enum

class ByType():
    """
    Set of supported locator strategies.
    """

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "linkText"
    PARTIAL_LINK_TEXT = "partialLinkText"
    NAME = "name"
    TAG_NAME = "tagName"
    CLASS_NAME = "className"
    CSS_SELECTOR = "cssSelector"