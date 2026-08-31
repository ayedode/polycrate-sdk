from typing import Literal

ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_kubernetes_apps_reconcile_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateProviderIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
