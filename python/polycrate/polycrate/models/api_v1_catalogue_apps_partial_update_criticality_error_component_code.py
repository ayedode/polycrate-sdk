from typing import Literal

ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_catalogue_apps_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
