from typing import Literal

ApiV1HostsReconcileCreateDefaultIpv4ErrorComponentAttr = Literal["default_ipv4"]

API_V1_HOSTS_RECONCILE_CREATE_DEFAULT_IPV_4_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateDefaultIpv4ErrorComponentAttr
] = {
    "default_ipv4",
}


def check_api_v1_hosts_reconcile_create_default_ipv_4_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateDefaultIpv4ErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_DEFAULT_IPV_4_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_DEFAULT_IPV_4_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
