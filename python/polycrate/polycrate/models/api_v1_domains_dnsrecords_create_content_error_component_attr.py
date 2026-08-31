from typing import Literal

ApiV1DomainsDnsrecordsCreateContentErrorComponentAttr = Literal["content"]

API_V1_DOMAINS_DNSRECORDS_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateContentErrorComponentAttr
] = {
    "content",
}


def check_api_v1_domains_dnsrecords_create_content_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateContentErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
