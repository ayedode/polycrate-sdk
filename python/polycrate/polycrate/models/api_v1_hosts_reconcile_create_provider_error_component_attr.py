from typing import Literal

ApiV1HostsReconcileCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_hosts_reconcile_create_provider_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateProviderErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
