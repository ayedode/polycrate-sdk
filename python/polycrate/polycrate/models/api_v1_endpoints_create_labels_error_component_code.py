from typing import Literal

ApiV1EndpointsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_endpoints_create_labels_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateLabelsErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
