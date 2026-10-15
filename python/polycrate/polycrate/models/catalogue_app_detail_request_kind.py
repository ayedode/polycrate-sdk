from typing import Literal

CatalogueAppDetailRequestKind = Literal["generic"]

CATALOGUE_APP_DETAIL_REQUEST_KIND_VALUES: set[CatalogueAppDetailRequestKind] = {
    "generic",
}


def check_catalogue_app_detail_request_kind(value: str) -> CatalogueAppDetailRequestKind:
    if value in CATALOGUE_APP_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_REQUEST_KIND_VALUES!r}")
