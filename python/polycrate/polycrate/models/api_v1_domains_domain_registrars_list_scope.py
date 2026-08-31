from typing import Literal

ApiV1DomainsDomainRegistrarsListScope = Literal["system", "user"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SCOPE_VALUES: set[ApiV1DomainsDomainRegistrarsListScope] = {
    "system",
    "user",
}


def check_api_v1_domains_domain_registrars_list_scope(value: str) -> ApiV1DomainsDomainRegistrarsListScope:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_SCOPE_VALUES!r}"
    )
