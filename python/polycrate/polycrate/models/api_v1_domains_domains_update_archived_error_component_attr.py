from typing import Literal

ApiV1DomainsDomainsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DOMAINS_DOMAINS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_domains_domains_update_archived_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateArchivedErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
