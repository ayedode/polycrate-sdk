from typing import Literal

PatchedCatalogueAppDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedCatalogueAppDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_catalogue_app_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedCatalogueAppDetailRequestCriticalityType3Type1:
    if value in PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
