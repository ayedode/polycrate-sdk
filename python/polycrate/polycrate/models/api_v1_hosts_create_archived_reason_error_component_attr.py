from typing import Literal

ApiV1HostsCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_HOSTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_hosts_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1HostsCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
