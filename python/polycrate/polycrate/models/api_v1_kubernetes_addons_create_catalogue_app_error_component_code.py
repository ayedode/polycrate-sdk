from typing import Literal

ApiV1KubernetesAddonsCreateCatalogueAppErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_KUBERNETES_ADDONS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsCreateCatalogueAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_kubernetes_addons_create_catalogue_app_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsCreateCatalogueAppErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
