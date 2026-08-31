from typing import Literal

ApiV1CertificatesUpdateNotBeforeErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CERTIFICATES_UPDATE_NOT_BEFORE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateNotBeforeErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_certificates_update_not_before_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateNotBeforeErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_NOT_BEFORE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_NOT_BEFORE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
