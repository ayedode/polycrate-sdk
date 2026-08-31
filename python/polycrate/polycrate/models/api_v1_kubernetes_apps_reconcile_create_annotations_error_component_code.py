from typing import Literal

ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_apps_reconcile_create_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
