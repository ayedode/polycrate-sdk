from typing import Literal

ApiV1CertificatesCreateSecretNameErrorComponentAttr = Literal["secret_name"]

API_V1_CERTIFICATES_CREATE_SECRET_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateSecretNameErrorComponentAttr
] = {
    "secret_name",
}


def check_api_v1_certificates_create_secret_name_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateSecretNameErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_SECRET_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_SECRET_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
