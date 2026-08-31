from typing import Literal

ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null", "required", "unique"
]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SERIAL_NUMBER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
    "required",
    "unique",
}


def check_api_v1_catalogue_apps_archive_create_serial_number_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SERIAL_NUMBER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_SERIAL_NUMBER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
