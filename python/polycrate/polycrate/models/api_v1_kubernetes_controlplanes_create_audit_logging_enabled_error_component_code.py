from typing import Literal

ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_AUDIT_LOGGING_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_controlplanes_create_audit_logging_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_AUDIT_LOGGING_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_AUDIT_LOGGING_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
