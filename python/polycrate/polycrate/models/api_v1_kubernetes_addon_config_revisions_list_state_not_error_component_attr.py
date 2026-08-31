from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_kubernetes_addon_config_revisions_list_state_not_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
