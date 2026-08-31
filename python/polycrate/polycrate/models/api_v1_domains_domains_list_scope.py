from typing import Literal

ApiV1DomainsDomainsListScope = Literal["system", "user"]

API_V1_DOMAINS_DOMAINS_LIST_SCOPE_VALUES: set[ApiV1DomainsDomainsListScope] = {
    "system",
    "user",
}


def check_api_v1_domains_domains_list_scope(value: str) -> ApiV1DomainsDomainsListScope:
    if value in API_V1_DOMAINS_DOMAINS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_SCOPE_VALUES!r}")
