from typing import Literal

PatchedCatalogueAppDetailRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[
    PatchedCatalogueAppDetailRequestCreatedByComponentType1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_catalogue_app_detail_request_created_by_component_type_1(
    value: str,
) -> PatchedCatalogueAppDetailRequestCreatedByComponentType1:
    if value in PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CATALOGUE_APP_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
