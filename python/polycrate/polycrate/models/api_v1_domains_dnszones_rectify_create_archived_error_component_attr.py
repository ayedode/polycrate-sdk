from typing import Literal

ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_domains_dnszones_rectify_create_archived_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
