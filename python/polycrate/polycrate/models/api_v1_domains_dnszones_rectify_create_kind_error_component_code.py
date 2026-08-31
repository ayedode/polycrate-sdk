from typing import Literal

ApiV1DomainsDnszonesRectifyCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_dnszones_rectify_create_kind_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateKindErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
