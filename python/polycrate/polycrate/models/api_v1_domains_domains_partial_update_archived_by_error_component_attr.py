from typing import Literal

ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_domains_domains_partial_update_archived_by_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
