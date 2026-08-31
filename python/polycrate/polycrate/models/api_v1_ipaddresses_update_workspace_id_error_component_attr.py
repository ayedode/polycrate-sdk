from typing import Literal

ApiV1IpaddressesUpdateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_IPADDRESSES_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesUpdateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_ipaddresses_update_workspace_id_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdateWorkspaceIdErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
