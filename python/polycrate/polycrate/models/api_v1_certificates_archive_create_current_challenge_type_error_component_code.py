from typing import Literal

ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CERTIFICATES_ARCHIVE_CREATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_archive_create_current_challenge_type_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateCurrentChallengeTypeErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
