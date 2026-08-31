from typing import Literal

ApiV1DomainsDnszonesListScope = Literal["system", "user"]

API_V1_DOMAINS_DNSZONES_LIST_SCOPE_VALUES: set[ApiV1DomainsDnszonesListScope] = {
    "system",
    "user",
}


def check_api_v1_domains_dnszones_list_scope(value: str) -> ApiV1DomainsDnszonesListScope:
    if value in API_V1_DOMAINS_DNSZONES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_SCOPE_VALUES!r}")
