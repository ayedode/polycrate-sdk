from typing import Literal

ApiV1CertificatesPartialUpdateSecretNameErrorComponentAttr = Literal["secret_name"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_SECRET_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateSecretNameErrorComponentAttr
] = {
    "secret_name",
}


def check_api_v1_certificates_partial_update_secret_name_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateSecretNameErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_SECRET_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_SECRET_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
