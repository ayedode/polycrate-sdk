from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_catalogue_apps_sync_releases_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
