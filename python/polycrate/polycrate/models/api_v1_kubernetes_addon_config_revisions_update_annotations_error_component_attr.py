from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_addon_config_revisions_update_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
