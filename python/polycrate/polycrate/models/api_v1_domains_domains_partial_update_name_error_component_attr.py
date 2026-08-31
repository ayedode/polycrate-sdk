from typing import Literal

ApiV1DomainsDomainsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_domains_domains_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
