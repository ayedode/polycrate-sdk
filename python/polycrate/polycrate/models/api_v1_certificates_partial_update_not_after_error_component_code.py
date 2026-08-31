from typing import Literal

ApiV1CertificatesPartialUpdateNotAfterErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_AFTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateNotAfterErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_certificates_partial_update_not_after_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateNotAfterErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_AFTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_NOT_AFTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
