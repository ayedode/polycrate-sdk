from typing import Literal

ApiV1CertificatesUpdateRenewalTimeErrorComponentAttr = Literal["renewal_time"]

API_V1_CERTIFICATES_UPDATE_RENEWAL_TIME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateRenewalTimeErrorComponentAttr
] = {
    "renewal_time",
}


def check_api_v1_certificates_update_renewal_time_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateRenewalTimeErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_RENEWAL_TIME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_RENEWAL_TIME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
