from typing import Literal

ApiV1KubernetesAppsCreateCatalogueAppErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsCreateCatalogueAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_create_catalogue_app_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsCreateCatalogueAppErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
