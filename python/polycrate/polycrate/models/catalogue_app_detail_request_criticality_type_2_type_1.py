from typing import Literal

CatalogueAppDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CatalogueAppDetailRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_catalogue_app_detail_request_criticality_type_2_type_1(
    value: str,
) -> CatalogueAppDetailRequestCriticalityType2Type1:
    if value in CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
