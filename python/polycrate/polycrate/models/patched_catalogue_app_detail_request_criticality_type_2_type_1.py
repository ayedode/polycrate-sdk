from typing import Literal

PatchedCatalogueAppDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedCatalogueAppDetailRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_catalogue_app_detail_request_criticality_type_2_type_1(
    value: str,
) -> PatchedCatalogueAppDetailRequestCriticalityType2Type1:
    if value in PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
