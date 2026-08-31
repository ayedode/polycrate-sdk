from typing import Literal

ApiV1DomainsDnsrecordsCreatePriorityErrorComponentAttr = Literal["priority"]

API_V1_DOMAINS_DNSRECORDS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_domains_dnsrecords_create_priority_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreatePriorityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
