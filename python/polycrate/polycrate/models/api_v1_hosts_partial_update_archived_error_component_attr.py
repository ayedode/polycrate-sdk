from typing import Literal

ApiV1HostsPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_HOSTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_hosts_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
