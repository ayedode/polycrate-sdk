from typing import Literal

ApiV1IpaddressesListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_IPADDRESSES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IpaddressesListStateNotErrorComponentAttr] = {
    "state_not",
}


def check_api_v1_ipaddresses_list_state_not_error_component_attr(
    value: str,
) -> ApiV1IpaddressesListStateNotErrorComponentAttr:
    if value in API_V1_IPADDRESSES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
