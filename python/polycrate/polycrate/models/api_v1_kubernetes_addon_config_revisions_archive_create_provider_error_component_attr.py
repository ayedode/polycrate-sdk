from typing import Literal

ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_kubernetes_addon_config_revisions_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
