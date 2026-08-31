from typing import Literal

ApiV1DomainsDnsrecordsListTypeErrorComponentAttr = Literal["type"]

API_V1_DOMAINS_DNSRECORDS_LIST_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsListTypeErrorComponentAttr
] = {
    "type",
}


def check_api_v1_domains_dnsrecords_list_type_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsListTypeErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
