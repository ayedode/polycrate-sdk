from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_addon_config_revisions_update_labels_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateLabelsErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
