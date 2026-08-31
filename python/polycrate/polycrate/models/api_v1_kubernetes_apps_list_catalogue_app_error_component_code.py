from typing import Literal

ApiV1KubernetesAppsListCatalogueAppErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_APPS_LIST_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsListCatalogueAppErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_apps_list_catalogue_app_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsListCatalogueAppErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_LIST_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
