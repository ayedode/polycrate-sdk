from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponentAttr = Literal["type"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponentAttr
] = {
    "type",
}


def check_api_v1_domains_dnsrecords_partial_update_type_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateTypeErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
