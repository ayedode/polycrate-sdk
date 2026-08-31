from typing import Literal

ApiV1HostsReconcileCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_HOSTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_hosts_reconcile_create_tolerations_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateTolerationsErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
