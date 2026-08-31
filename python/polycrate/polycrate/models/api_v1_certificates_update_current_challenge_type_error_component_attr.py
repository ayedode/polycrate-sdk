from typing import Literal

ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponentAttr = Literal["current_challenge_type"]

API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponentAttr
] = {
    "current_challenge_type",
}


def check_api_v1_certificates_update_current_challenge_type_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateCurrentChallengeTypeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
