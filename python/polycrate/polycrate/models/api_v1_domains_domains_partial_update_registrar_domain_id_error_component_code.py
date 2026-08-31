from typing import Literal

ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_DOMAIN_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_domains_partial_update_registrar_domain_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_DOMAIN_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_DOMAIN_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
