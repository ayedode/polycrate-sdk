from typing import Literal

ApiV1IpaddressesUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_IPADDRESSES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_ipaddresses_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
