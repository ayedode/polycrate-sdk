from typing import Literal

ApiV1KubernetesAddonsCreateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_KUBERNETES_ADDONS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_kubernetes_addons_create_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateCatalogueAppErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
