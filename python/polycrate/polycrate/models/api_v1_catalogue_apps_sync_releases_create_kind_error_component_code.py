from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_catalogue_apps_sync_releases_create_kind_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
