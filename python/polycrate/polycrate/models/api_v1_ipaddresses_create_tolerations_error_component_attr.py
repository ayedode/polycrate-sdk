from typing import Literal

ApiV1IpaddressesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_IPADDRESSES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_ipaddresses_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1IpaddressesCreateTolerationsErrorComponentAttr:
    if value in API_V1_IPADDRESSES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
