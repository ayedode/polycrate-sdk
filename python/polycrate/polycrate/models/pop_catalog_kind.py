from typing import Literal

PopCatalogKind = Literal["datacenter", "datacenter-park", "region"]

POP_CATALOG_KIND_VALUES: set[PopCatalogKind] = {
    "datacenter",
    "datacenter-park",
    "region",
}


def check_pop_catalog_kind(value: str) -> PopCatalogKind:
    if value in POP_CATALOG_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_KIND_VALUES!r}")
