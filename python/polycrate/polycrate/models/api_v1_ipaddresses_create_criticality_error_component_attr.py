from typing import Literal

ApiV1IpaddressesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_IPADDRESSES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_ipaddresses_create_criticality_error_component_attr(
    value: str,
) -> ApiV1IpaddressesCreateCriticalityErrorComponentAttr:
    if value in API_V1_IPADDRESSES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
