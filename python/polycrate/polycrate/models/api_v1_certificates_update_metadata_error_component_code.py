from typing import Literal

ApiV1CertificatesUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_update_metadata_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateMetadataErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
