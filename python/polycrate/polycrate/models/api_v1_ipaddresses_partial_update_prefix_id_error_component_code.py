from typing import Literal

ApiV1IpaddressesPartialUpdatePrefixIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_IPADDRESSES_PARTIAL_UPDATE_PREFIX_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesPartialUpdatePrefixIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_ipaddresses_partial_update_prefix_id_error_component_code(
    value: str,
) -> ApiV1IpaddressesPartialUpdatePrefixIdErrorComponentCode:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_PREFIX_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_PREFIX_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
