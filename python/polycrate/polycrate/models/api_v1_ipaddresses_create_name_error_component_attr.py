from typing import Literal

ApiV1IpaddressesCreateNameErrorComponentAttr = Literal["name"]

API_V1_IPADDRESSES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_ipaddresses_create_name_error_component_attr(
    value: str,
) -> ApiV1IpaddressesCreateNameErrorComponentAttr:
    if value in API_V1_IPADDRESSES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
