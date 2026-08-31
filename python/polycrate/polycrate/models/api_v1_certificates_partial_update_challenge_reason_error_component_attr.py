from typing import Literal

ApiV1CertificatesPartialUpdateChallengeReasonErrorComponentAttr = Literal["challenge_reason"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_CHALLENGE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateChallengeReasonErrorComponentAttr
] = {
    "challenge_reason",
}


def check_api_v1_certificates_partial_update_challenge_reason_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateChallengeReasonErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_CHALLENGE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_CHALLENGE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
