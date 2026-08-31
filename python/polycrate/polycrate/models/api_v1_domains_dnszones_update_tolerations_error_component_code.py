from typing import Literal

ApiV1DomainsDnszonesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_update_tolerations_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesUpdateTolerationsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
