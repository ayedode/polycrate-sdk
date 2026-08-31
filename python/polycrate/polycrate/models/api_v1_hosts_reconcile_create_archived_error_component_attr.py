from typing import Literal

ApiV1HostsReconcileCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_HOSTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_hosts_reconcile_create_archived_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateArchivedErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
