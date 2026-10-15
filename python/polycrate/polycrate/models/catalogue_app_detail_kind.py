from typing import Literal

CatalogueAppDetailKind = Literal["generic"]

CATALOGUE_APP_DETAIL_KIND_VALUES: set[CatalogueAppDetailKind] = {
    "generic",
}


def check_catalogue_app_detail_kind(value: str) -> CatalogueAppDetailKind:
    if value in CATALOGUE_APP_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_KIND_VALUES!r}")
