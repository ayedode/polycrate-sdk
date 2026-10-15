from typing import Literal

CatalogueAppDetailScope = Literal["system", "user"]

CATALOGUE_APP_DETAIL_SCOPE_VALUES: set[CatalogueAppDetailScope] = {
    "system",
    "user",
}


def check_catalogue_app_detail_scope(value: str) -> CatalogueAppDetailScope:
    if value in CATALOGUE_APP_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_SCOPE_VALUES!r}")
