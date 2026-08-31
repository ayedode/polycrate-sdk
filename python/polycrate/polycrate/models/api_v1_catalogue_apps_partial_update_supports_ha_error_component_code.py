from typing import Literal

ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_partial_update_supports_ha_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
