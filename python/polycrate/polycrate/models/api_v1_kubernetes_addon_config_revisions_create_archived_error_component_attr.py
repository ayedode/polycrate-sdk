from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_addon_config_revisions_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
