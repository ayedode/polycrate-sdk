from typing import Literal

ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_kubernetes_addon_config_revisions_partial_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
