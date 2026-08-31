from typing import Literal

ApiV1CertificatesArchiveCreateChallengeReasonErrorComponentAttr = Literal["challenge_reason"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_CHALLENGE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateChallengeReasonErrorComponentAttr
] = {
    "challenge_reason",
}


def check_api_v1_certificates_archive_create_challenge_reason_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateChallengeReasonErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_CHALLENGE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_CHALLENGE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
