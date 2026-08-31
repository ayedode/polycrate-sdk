from typing import Literal

ApiV1EndpointsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ENDPOINTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_endpoints_update_annotations_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
