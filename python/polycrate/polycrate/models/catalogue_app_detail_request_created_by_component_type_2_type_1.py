from typing import Literal

CatalogueAppDetailRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

CATALOGUE_APP_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[
    CatalogueAppDetailRequestCreatedByComponentType2Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_catalogue_app_detail_request_created_by_component_type_2_type_1(
    value: str,
) -> CatalogueAppDetailRequestCreatedByComponentType2Type1:
    if value in CATALOGUE_APP_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
