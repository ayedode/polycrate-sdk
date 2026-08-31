from typing import Literal

ApiV1CatalogueAppsCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CATALOGUE_APPS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CatalogueAppsCreateNameErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_catalogue_apps_create_name_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsCreateNameErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
