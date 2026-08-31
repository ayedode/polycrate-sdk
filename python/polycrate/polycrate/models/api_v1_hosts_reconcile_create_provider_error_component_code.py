from typing import Literal

ApiV1HostsReconcileCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_hosts_reconcile_create_provider_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateProviderErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
