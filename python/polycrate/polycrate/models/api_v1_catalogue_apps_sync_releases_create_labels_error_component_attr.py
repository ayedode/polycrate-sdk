from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_catalogue_apps_sync_releases_create_labels_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
