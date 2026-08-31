from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_kubernetes_addon_config_revisions_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateProviderIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
