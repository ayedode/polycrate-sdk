from typing import Literal

ApiV1HostsReconcileCreateRoleErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_HOSTS_RECONCILE_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsReconcileCreateRoleErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_hosts_reconcile_create_role_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateRoleErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
