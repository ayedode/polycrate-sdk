from typing import Literal

ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_discover_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1HostsDiscoverCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_HOSTS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
