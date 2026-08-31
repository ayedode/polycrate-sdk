from typing import Literal

ApiV1EndpointsListKindErrorComponentAttr = Literal["kind"]

API_V1_ENDPOINTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_endpoints_list_kind_error_component_attr(value: str) -> ApiV1EndpointsListKindErrorComponentAttr:
    if value in API_V1_ENDPOINTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
