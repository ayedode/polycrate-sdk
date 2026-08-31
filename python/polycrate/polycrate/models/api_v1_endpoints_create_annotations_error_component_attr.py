from typing import Literal

ApiV1EndpointsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ENDPOINTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_endpoints_create_annotations_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
