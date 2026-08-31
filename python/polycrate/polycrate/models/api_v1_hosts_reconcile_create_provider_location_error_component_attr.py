from typing import Literal

ApiV1HostsReconcileCreateProviderLocationErrorComponentAttr = Literal["provider_location"]

API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateProviderLocationErrorComponentAttr
] = {
    "provider_location",
}


def check_api_v1_hosts_reconcile_create_provider_location_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateProviderLocationErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
