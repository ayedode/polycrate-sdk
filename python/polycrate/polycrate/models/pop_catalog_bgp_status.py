from typing import Literal

PopCatalogBgpStatus = Literal["no", "planned", "unknown", "yes"]

POP_CATALOG_BGP_STATUS_VALUES: set[PopCatalogBgpStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_catalog_bgp_status(value: str) -> PopCatalogBgpStatus:
    if value in POP_CATALOG_BGP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_BGP_STATUS_VALUES!r}")
