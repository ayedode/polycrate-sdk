from typing import Literal

ApiV1IpaddressesPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_IPADDRESSES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_ipaddresses_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1IpaddressesPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
