from typing import Literal

ApiV1DomainsDnszonesListNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DNSZONES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DomainsDnszonesListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_domains_dnszones_list_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesListNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
