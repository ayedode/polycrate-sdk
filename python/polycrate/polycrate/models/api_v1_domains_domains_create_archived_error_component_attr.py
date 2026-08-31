from typing import Literal

ApiV1DomainsDomainsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_domains_domains_create_archived_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateArchivedErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
