from typing import Literal

PopCatalogC5Status = Literal["none", "planned", "typ1", "typ2"]

POP_CATALOG_C5_STATUS_VALUES: set[PopCatalogC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_pop_catalog_c5_status(value: str) -> PopCatalogC5Status:
    if value in POP_CATALOG_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_C5_STATUS_VALUES!r}")
