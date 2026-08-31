from typing import Literal

ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponentAttr = Literal["current_challenge_status"]

API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponentAttr
] = {
    "current_challenge_status",
}


def check_api_v1_certificates_update_current_challenge_status_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateCurrentChallengeStatusErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
