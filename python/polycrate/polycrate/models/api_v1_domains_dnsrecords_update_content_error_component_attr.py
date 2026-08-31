from typing import Literal

ApiV1DomainsDnsrecordsUpdateContentErrorComponentAttr = Literal["content"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateContentErrorComponentAttr
] = {
    "content",
}


def check_api_v1_domains_dnsrecords_update_content_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateContentErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
