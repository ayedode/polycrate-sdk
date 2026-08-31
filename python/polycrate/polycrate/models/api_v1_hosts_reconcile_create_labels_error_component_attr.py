from typing import Literal

ApiV1HostsReconcileCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_HOSTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_hosts_reconcile_create_labels_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateLabelsErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
