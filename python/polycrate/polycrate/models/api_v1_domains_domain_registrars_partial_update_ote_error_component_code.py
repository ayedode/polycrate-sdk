from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_OTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domain_registrars_partial_update_ote_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_OTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_OTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
