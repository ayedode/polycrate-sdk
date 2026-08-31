from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_kubernetes_addon_config_revisions_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
