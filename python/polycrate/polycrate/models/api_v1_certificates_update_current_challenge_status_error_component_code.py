from typing import Literal

ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_update_current_challenge_status_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
