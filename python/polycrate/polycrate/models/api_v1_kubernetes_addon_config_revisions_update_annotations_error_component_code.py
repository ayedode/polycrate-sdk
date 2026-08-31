from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_addon_config_revisions_update_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
