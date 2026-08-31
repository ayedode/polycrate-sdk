from typing import Literal

ApiV1CvesCreateCvssVectorErrorComponentAttr = Literal["cvss_vector"]

API_V1_CVES_CREATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateCvssVectorErrorComponentAttr] = {
    "cvss_vector",
}


def check_api_v1_cves_create_cvss_vector_error_component_attr(
    value: str,
) -> ApiV1CvesCreateCvssVectorErrorComponentAttr:
    if value in API_V1_CVES_CREATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CVSS_VECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
