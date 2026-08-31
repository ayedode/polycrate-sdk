from typing import Literal

ApiV1AlertroutersArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_alertrouters_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
