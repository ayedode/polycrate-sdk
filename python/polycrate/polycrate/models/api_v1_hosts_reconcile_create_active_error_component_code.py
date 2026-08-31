from typing import Literal

ApiV1HostsReconcileCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_reconcile_create_active_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateActiveErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
