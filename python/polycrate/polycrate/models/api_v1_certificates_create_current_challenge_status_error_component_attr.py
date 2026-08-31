from typing import Literal

ApiV1CertificatesCreateCurrentChallengeStatusErrorComponentAttr = Literal["current_challenge_status"]

API_V1_CERTIFICATES_CREATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateCurrentChallengeStatusErrorComponentAttr
] = {
    "current_challenge_status",
}


def check_api_v1_certificates_create_current_challenge_status_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateCurrentChallengeStatusErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
