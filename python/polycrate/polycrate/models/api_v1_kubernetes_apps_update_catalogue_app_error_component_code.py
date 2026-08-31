from typing import Literal

ApiV1KubernetesAppsUpdateCatalogueAppErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUpdateCatalogueAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_update_catalogue_app_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdateCatalogueAppErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
