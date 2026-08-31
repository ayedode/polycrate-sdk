from typing import Literal

ApiV1DomainsDnszonesCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_DOMAINS_DNSZONES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_domains_dnszones_create_display_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesCreateDisplayNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
