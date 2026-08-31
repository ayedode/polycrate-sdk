from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_catalogue_apps_sync_releases_create_annotations_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
