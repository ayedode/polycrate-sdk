from typing import Literal

ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_kubernetes_apps_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
