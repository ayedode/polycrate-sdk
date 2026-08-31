from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_kubernetes_addon_config_revisions_list_created_by_component(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
