from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_catalogue_apps_sync_releases_create_annotations_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
