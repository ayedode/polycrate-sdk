from typing import Literal

ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_catalogue_apps_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
