from typing import Literal

ApiV1HostsReconcileCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_HOSTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_hosts_reconcile_create_labels_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateLabelsErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
