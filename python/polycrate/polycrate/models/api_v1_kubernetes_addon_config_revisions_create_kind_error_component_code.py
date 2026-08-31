from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_addon_config_revisions_create_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateKindErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
