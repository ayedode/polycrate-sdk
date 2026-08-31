from typing import Literal

ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponentAttr = Literal[
    "last_reconciliation_duration_seconds"
]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponentAttr
] = {
    "last_reconciliation_duration_seconds",
}


def check_api_v1_kubernetes_apps_discover_create_last_reconciliation_duration_seconds_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateLastReconciliationDurationSecondsErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
