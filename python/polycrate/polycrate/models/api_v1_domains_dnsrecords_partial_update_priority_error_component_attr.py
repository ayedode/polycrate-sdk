from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponentAttr = Literal["priority"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_domains_dnsrecords_partial_update_priority_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdatePriorityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
