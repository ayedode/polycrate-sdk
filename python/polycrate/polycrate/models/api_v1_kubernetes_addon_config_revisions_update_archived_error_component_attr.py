from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_addon_config_revisions_update_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
