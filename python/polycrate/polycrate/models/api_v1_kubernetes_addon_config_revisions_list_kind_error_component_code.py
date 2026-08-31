from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListKindErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListKindErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_kubernetes_addon_config_revisions_list_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListKindErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
