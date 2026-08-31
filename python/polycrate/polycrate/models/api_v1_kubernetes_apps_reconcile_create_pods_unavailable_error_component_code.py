from typing import Literal

ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_kubernetes_apps_reconcile_create_pods_unavailable_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreatePodsUnavailableErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
