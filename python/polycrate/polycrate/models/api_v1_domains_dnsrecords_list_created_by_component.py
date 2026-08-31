from typing import Literal

ApiV1DomainsDnsrecordsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1DomainsDnsrecordsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_domains_dnsrecords_list_created_by_component(
    value: str,
) -> ApiV1DomainsDnsrecordsListCreatedByComponent:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
