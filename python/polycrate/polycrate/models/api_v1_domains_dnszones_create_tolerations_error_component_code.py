from typing import Literal

ApiV1DomainsDnszonesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_create_tolerations_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesCreateTolerationsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
