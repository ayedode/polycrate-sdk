from typing import Literal

ApiV1DomainsDnsrecordsCreateNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DNSRECORDS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_domains_dnsrecords_create_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
