from typing import Literal

ApiV1DomainsDnszonesCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DNSZONES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_dnszones_create_criticality_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesCreateCriticalityErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
