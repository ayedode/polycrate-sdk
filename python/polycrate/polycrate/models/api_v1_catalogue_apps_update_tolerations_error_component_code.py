from typing import Literal

ApiV1CatalogueAppsUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_update_tolerations_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsUpdateTolerationsErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
