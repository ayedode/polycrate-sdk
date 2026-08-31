from typing import Literal

ApiV1KubernetesAppsReconcileCreateByoaErrorComponentAttr = Literal["byoa"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateByoaErrorComponentAttr
] = {
    "byoa",
}


def check_api_v1_kubernetes_apps_reconcile_create_byoa_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateByoaErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
