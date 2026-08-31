from typing import Literal

ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
