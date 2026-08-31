from typing import Literal

ApiV1DomainsDnszonesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_DOMAINS_DNSZONES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_domains_dnszones_list_organizations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesListOrganizationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
