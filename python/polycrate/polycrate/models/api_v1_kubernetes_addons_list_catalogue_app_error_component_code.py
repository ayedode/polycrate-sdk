from typing import Literal

ApiV1KubernetesAddonsListCatalogueAppErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_KUBERNETES_ADDONS_LIST_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsListCatalogueAppErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_list_catalogue_app_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsListCatalogueAppErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_LIST_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
