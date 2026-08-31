from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_kubernetes_addon_config_revisions_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
