from typing import Literal

ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_apps_reconcile_create_excluded_from_downtime_until_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateExcludedFromDowntimeUntilErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
