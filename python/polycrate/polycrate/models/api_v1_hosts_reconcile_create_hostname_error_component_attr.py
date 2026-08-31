from typing import Literal

ApiV1HostsReconcileCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_HOSTS_RECONCILE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_hosts_reconcile_create_hostname_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateHostnameErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
