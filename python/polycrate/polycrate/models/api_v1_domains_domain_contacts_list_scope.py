from typing import Literal

ApiV1DomainsDomainContactsListScope = Literal["system", "user"]

API_V1_DOMAINS_DOMAIN_CONTACTS_LIST_SCOPE_VALUES: set[ApiV1DomainsDomainContactsListScope] = {
    "system",
    "user",
}


def check_api_v1_domains_domain_contacts_list_scope(value: str) -> ApiV1DomainsDomainContactsListScope:
    if value in API_V1_DOMAINS_DOMAIN_CONTACTS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_CONTACTS_LIST_SCOPE_VALUES!r}")
