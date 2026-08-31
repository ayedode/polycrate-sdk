from typing import Literal

ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_kubernetes_apps_reconcile_create_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateCatalogueAppErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
