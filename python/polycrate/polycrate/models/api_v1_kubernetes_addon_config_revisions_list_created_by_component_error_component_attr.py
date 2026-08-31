from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_kubernetes_addon_config_revisions_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListCreatedByComponentErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
