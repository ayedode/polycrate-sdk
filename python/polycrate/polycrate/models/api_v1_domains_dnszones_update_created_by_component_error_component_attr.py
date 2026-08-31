from typing import Literal

ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_DOMAINS_DNSZONES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_domains_dnszones_update_created_by_component_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateCreatedByComponentErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
