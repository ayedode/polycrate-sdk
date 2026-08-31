from typing import Literal

ApiV1CertificatesPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
