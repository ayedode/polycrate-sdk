from typing import Literal

ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_kubernetes_apps_partial_update_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateCatalogueAppErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
