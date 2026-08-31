from typing import Literal

ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_domains_dnszones_rectify_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
