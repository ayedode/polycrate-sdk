from typing import Literal

ApiV1IpaddressesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_IPADDRESSES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_ipaddresses_update_kind_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdateKindErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
