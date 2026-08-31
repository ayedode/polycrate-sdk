from typing import Literal

ApiV1CatalogueAppsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_CATALOGUE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_catalogue_apps_update_criticality_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsUpdateCriticalityErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
