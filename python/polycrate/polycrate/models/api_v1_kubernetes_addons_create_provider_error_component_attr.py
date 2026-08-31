from typing import Literal

ApiV1KubernetesAddonsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_KUBERNETES_ADDONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_kubernetes_addons_create_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
