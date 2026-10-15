from typing import Literal

CatalogueAppDetailCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

CATALOGUE_APP_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[CatalogueAppDetailCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_catalogue_app_detail_created_by_component_type_1(value: str) -> CatalogueAppDetailCreatedByComponentType1:
    if value in CATALOGUE_APP_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
