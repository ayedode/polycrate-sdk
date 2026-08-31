from typing import Literal

ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_kubernetes_apps_discover_create_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateCatalogueAppErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
