from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_addon_config_revisions_list_created_at_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListCreatedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
