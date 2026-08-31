from typing import Literal

ApiV1HostsReconcileCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_HOSTS_RECONCILE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_hosts_reconcile_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateArchivedAtErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
