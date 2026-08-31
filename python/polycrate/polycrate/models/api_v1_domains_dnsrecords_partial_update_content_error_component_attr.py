from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponentAttr = Literal["content"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponentAttr
] = {
    "content",
}


def check_api_v1_domains_dnsrecords_partial_update_content_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateContentErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
