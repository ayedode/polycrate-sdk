from typing import Literal

ApiV1EndpointsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_update_annotations_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
