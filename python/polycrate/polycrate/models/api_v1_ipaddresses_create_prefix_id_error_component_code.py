from typing import Literal

ApiV1IpaddressesCreatePrefixIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null", "required"]

API_V1_IPADDRESSES_CREATE_PREFIX_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesCreatePrefixIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_ipaddresses_create_prefix_id_error_component_code(
    value: str,
) -> ApiV1IpaddressesCreatePrefixIdErrorComponentCode:
    if value in API_V1_IPADDRESSES_CREATE_PREFIX_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_PREFIX_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
