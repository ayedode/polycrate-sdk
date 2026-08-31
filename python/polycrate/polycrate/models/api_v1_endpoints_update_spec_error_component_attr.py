from typing import Literal

ApiV1EndpointsUpdateSpecErrorComponentAttr = Literal["spec"]

API_V1_ENDPOINTS_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsUpdateSpecErrorComponentAttr] = {
    "spec",
}


def check_api_v1_endpoints_update_spec_error_component_attr(value: str) -> ApiV1EndpointsUpdateSpecErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
