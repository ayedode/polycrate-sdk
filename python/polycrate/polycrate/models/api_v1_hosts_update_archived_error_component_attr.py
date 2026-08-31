from typing import Literal

ApiV1HostsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_HOSTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_hosts_update_archived_error_component_attr(value: str) -> ApiV1HostsUpdateArchivedErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
