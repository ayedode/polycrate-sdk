from typing import Literal

ApiV1KubernetesAppsReconcileCreateSourceErrorComponentAttr = Literal["source"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateSourceErrorComponentAttr
] = {
    "source",
}


def check_api_v1_kubernetes_apps_reconcile_create_source_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateSourceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
