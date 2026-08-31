from typing import Literal

ApiV1EndpointsPartialUpdateSpecErrorComponentAttr = Literal["spec"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateSpecErrorComponentAttr
] = {
    "spec",
}


def check_api_v1_endpoints_partial_update_spec_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateSpecErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
