from typing import Literal

ApiV1DomainsDomainsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DOMAINS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DomainsDomainsUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_domains_domains_update_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
