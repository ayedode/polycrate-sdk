from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_addon_config_revisions_list_search_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListSearchErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
