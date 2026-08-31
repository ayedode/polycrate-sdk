from typing import Literal

ApiV1KubernetesAppsListCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_KUBERNETES_APPS_LIST_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsListCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_kubernetes_apps_list_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListCatalogueAppErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
