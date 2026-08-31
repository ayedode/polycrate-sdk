from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_addon_config_revisions_list_state_not_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListStateNotErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
