from typing import Literal

ApiV1CatalogueAppsCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CATALOGUE_APPS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CatalogueAppsCreateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_catalogue_apps_create_kind_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateKindErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
