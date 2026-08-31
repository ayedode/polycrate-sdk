from typing import Literal

ApiV1DomainsDomainsCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_domains_domains_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
