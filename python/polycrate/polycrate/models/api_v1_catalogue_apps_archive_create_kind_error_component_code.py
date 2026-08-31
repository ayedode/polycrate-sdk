from typing import Literal

ApiV1CatalogueAppsArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_catalogue_apps_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateKindErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
