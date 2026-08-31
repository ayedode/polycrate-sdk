from typing import Literal

ApiV1DatasourcesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DATASOURCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_datasources_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
