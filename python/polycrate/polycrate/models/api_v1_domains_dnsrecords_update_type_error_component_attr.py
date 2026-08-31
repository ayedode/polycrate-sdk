from typing import Literal

ApiV1DomainsDnsrecordsUpdateTypeErrorComponentAttr = Literal["type"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateTypeErrorComponentAttr
] = {
    "type",
}


def check_api_v1_domains_dnsrecords_update_type_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateTypeErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
