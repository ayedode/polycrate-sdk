from typing import Literal

ApiV1HostsPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_HOSTS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_hosts_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
