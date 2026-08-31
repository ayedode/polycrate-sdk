from typing import Literal

ApiV1EndpointsDiscoverCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ENDPOINTS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_endpoints_discover_create_annotations_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
