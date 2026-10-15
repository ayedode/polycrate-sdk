from typing import Literal

PopCatalogIso27001Status = Literal["no", "planned", "unknown", "yes"]

POP_CATALOG_ISO_27001_STATUS_VALUES: set[PopCatalogIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_catalog_iso_27001_status(value: str) -> PopCatalogIso27001Status:
    if value in POP_CATALOG_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_ISO_27001_STATUS_VALUES!r}")
