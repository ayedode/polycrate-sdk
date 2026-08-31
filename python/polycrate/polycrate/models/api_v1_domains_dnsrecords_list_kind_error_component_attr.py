from typing import Literal

ApiV1DomainsDnsrecordsListKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DNSRECORDS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_dnsrecords_list_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsListKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
