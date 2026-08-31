from typing import Literal

ApiV1CertificatesPartialUpdateArchivedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateArchivedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_partial_update_archived_reason_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateArchivedReasonErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
