from typing import Literal

ApiV1IpaddressesUpdatePrefixIdErrorComponentAttr = Literal["prefix_id"]

API_V1_IPADDRESSES_UPDATE_PREFIX_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesUpdatePrefixIdErrorComponentAttr
] = {
    "prefix_id",
}


def check_api_v1_ipaddresses_update_prefix_id_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdatePrefixIdErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_PREFIX_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_PREFIX_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
