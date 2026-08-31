from typing import Literal

ApiV1IpaddressesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_IPADDRESSES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_ipaddresses_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
