from typing import Literal

ApiV1CertificatesCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_CERTIFICATES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_certificates_create_metadata_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateMetadataErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
