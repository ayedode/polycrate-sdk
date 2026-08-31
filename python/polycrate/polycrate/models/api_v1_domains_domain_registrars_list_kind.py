from typing import Literal

ApiV1DomainsDomainRegistrarsListKind = Literal["centralnic"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_KIND_VALUES: set[ApiV1DomainsDomainRegistrarsListKind] = {
    "centralnic",
}


def check_api_v1_domains_domain_registrars_list_kind(value: str) -> ApiV1DomainsDomainRegistrarsListKind:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_KIND_VALUES!r}"
    )
