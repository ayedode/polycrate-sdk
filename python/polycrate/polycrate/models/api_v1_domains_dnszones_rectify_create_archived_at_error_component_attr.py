from typing import Literal

ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_domains_dnszones_rectify_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
