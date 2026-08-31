from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ADDON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_kubernetes_addon_config_revisions_create_addon_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateAddonErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ADDON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_ADDON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
