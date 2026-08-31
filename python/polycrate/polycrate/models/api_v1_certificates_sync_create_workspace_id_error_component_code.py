from typing import Literal

ApiV1CertificatesSyncCreateWorkspaceIdErrorComponentCode = Literal["invalid", "max_string_length"]

API_V1_CERTIFICATES_SYNC_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesSyncCreateWorkspaceIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
}


def check_api_v1_certificates_sync_create_workspace_id_error_component_code(
    value: str,
) -> ApiV1CertificatesSyncCreateWorkspaceIdErrorComponentCode:
    if value in API_V1_CERTIFICATES_SYNC_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_SYNC_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
