from typing import Literal

ApiV1HostsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_HOSTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateArchivedAtErrorComponentAttr] = {
    "archived_at",
}


def check_api_v1_hosts_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
