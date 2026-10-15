from typing import Literal

PopCatalogEn50600Status = Literal["no", "planned", "unknown", "yes"]

POP_CATALOG_EN_50600_STATUS_VALUES: set[PopCatalogEn50600Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_catalog_en_50600_status(value: str) -> PopCatalogEn50600Status:
    if value in POP_CATALOG_EN_50600_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_EN_50600_STATUS_VALUES!r}")
