from typing import Literal

ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponentAttr = Literal["catalogue_app"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponentAttr
] = {
    "catalogue_app",
}


def check_api_v1_kubernetes_addons_partial_update_catalogue_app_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateCatalogueAppErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_CATALOGUE_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
