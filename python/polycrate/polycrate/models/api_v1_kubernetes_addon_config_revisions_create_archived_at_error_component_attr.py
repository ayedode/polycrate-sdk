from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_kubernetes_addon_config_revisions_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateArchivedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
