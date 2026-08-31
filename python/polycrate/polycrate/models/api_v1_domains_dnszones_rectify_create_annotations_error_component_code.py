from typing import Literal

ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_rectify_create_annotations_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
