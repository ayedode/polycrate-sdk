from typing import Literal

ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponentAttr = Literal["excluded_from_downtime_until"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponentAttr
] = {
    "excluded_from_downtime_until",
}


def check_api_v1_kubernetes_apps_reconcile_create_excluded_from_downtime_until_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
