from typing import Literal

ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_catalogue_apps_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
