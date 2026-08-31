from typing import Literal

ApiV1DomainsDnszonesCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_DOMAINS_DNSZONES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_domains_dnszones_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesCreateArchivedByErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
