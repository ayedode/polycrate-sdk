from typing import Literal

ApiV1DomainsDnszonesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DNSZONES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_dnszones_create_kind_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesCreateKindErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
