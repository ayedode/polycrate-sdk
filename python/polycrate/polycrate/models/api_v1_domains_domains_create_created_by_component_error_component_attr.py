from typing import Literal

ApiV1DomainsDomainsCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_DOMAINS_DOMAINS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_domains_domains_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
