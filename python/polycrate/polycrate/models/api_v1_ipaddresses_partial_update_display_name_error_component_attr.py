from typing import Literal

ApiV1IpaddressesPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_IPADDRESSES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_ipaddresses_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1IpaddressesPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
