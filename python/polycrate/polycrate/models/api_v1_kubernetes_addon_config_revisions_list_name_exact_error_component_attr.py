from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_kubernetes_addon_config_revisions_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListNameExactErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
