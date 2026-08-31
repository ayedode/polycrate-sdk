from typing import Literal

ApiV1CatalogueAppsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_catalogue_apps_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
