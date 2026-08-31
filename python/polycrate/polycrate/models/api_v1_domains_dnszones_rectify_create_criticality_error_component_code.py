from typing import Literal

ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_dnszones_rectify_create_criticality_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
