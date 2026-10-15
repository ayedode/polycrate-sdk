from typing import Literal

PatchedCatalogueAppDetailRequestKind = Literal["generic"]

PATCHED_CATALOGUE_APP_DETAIL_REQUEST_KIND_VALUES: set[PatchedCatalogueAppDetailRequestKind] = {
    "generic",
}


def check_patched_catalogue_app_detail_request_kind(value: str) -> PatchedCatalogueAppDetailRequestKind:
    if value in PATCHED_CATALOGUE_APP_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CATALOGUE_APP_DETAIL_REQUEST_KIND_VALUES!r}")
