from typing import Literal

ApiV1EndpointsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_endpoints_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
