from typing import Literal

ApiV1CertificatesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CERTIFICATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_certificates_update_annotations_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
