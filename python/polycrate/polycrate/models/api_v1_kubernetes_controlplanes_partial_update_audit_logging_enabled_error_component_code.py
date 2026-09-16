from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_AUDIT_LOGGING_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_controlplanes_partial_update_audit_logging_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_AUDIT_LOGGING_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_AUDIT_LOGGING_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
