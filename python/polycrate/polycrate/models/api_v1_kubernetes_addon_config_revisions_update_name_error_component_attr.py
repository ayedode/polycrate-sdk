from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_addon_config_revisions_update_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
