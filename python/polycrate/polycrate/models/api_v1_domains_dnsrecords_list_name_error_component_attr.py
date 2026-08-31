from typing import Literal

ApiV1DomainsDnsrecordsListNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DNSRECORDS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_domains_dnsrecords_list_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsListNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
