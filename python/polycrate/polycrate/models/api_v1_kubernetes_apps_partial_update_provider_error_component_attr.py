from typing import Literal

ApiV1KubernetesAppsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_kubernetes_apps_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
