from typing import Literal

ApiV1CertificatesSyncCreateOrganizationIdErrorComponentCode = Literal[
    "invalid", "max_string_length", "null", "required"
]

API_V1_CERTIFICATES_SYNC_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesSyncCreateOrganizationIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "null",
    "required",
}


def check_api_v1_certificates_sync_create_organization_id_error_component_code(
    value: str,
) -> ApiV1CertificatesSyncCreateOrganizationIdErrorComponentCode:
    if value in API_V1_CERTIFICATES_SYNC_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_SYNC_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
