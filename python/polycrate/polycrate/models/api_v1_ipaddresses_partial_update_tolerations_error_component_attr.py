from typing import Literal

ApiV1IpaddressesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_IPADDRESSES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_ipaddresses_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1IpaddressesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
