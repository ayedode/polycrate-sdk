from typing import Literal

ApiV1DomainsDnsrecordsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_domains_dnsrecords_update_archived_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateArchivedErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
