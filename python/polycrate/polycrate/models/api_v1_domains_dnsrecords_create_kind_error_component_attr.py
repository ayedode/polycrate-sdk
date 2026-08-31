from typing import Literal

ApiV1DomainsDnsrecordsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DNSRECORDS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_dnsrecords_create_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
