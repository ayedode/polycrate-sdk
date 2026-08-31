from typing import Literal

ApiV1CertificatesCreateCurrentChallengeTypeErrorComponentAttr = Literal["current_challenge_type"]

API_V1_CERTIFICATES_CREATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateCurrentChallengeTypeErrorComponentAttr
] = {
    "current_challenge_type",
}


def check_api_v1_certificates_create_current_challenge_type_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateCurrentChallengeTypeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_CURRENT_CHALLENGE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
