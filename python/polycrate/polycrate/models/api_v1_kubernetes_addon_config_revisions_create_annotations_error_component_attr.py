from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_addon_config_revisions_create_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
