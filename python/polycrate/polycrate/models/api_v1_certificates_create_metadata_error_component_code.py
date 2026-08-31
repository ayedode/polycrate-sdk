from typing import Literal

ApiV1CertificatesCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_create_metadata_error_component_code(
    value: str,
) -> ApiV1CertificatesCreateMetadataErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
