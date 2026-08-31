from typing import Literal

ApiV1DomainsDnsrecordsListScope = Literal["system", "user"]

API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_VALUES: set[ApiV1DomainsDnsrecordsListScope] = {
    "system",
    "user",
}


def check_api_v1_domains_dnsrecords_list_scope(value: str) -> ApiV1DomainsDnsrecordsListScope:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_SCOPE_VALUES!r}")
