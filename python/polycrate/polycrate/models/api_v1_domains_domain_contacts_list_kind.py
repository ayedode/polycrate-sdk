from typing import Literal

ApiV1DomainsDomainContactsListKind = Literal["organization", "person"]

API_V1_DOMAINS_DOMAIN_CONTACTS_LIST_KIND_VALUES: set[ApiV1DomainsDomainContactsListKind] = {
    "organization",
    "person",
}


def check_api_v1_domains_domain_contacts_list_kind(value: str) -> ApiV1DomainsDomainContactsListKind:
    if value in API_V1_DOMAINS_DOMAIN_CONTACTS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_CONTACTS_LIST_KIND_VALUES!r}")
