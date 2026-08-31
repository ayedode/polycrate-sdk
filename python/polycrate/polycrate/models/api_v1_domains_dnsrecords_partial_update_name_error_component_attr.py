from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_domains_dnsrecords_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
