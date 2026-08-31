from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domain_registrars_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
