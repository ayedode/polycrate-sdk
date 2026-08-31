from typing import Literal

ApiV1HostsReconcileCreateActiveErrorComponentAttr = Literal["active"]

API_V1_HOSTS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_hosts_reconcile_create_active_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateActiveErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
