from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_addon_config_revisions_list_name_exact_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
