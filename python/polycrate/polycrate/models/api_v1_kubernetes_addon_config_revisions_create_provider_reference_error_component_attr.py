from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_kubernetes_addon_config_revisions_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
