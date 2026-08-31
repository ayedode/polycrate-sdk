from typing import Literal

ApiV1CertificatesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_CERTIFICATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_certificates_update_annotations_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
