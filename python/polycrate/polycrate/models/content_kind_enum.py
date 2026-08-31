from typing import Literal

ContentKindEnum = Literal["html", "json", "markdown", "text", "yaml"]

CONTENT_KIND_ENUM_VALUES: set[ContentKindEnum] = {
    "html",
    "json",
    "markdown",
    "text",
    "yaml",
}


def check_content_kind_enum(value: str) -> ContentKindEnum:
    if value in CONTENT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTENT_KIND_ENUM_VALUES!r}")
