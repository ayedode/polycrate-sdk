from typing import Literal

ApiV1CatalogueAppsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_CATALOGUE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_catalogue_apps_create_criticality_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateCriticalityErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
