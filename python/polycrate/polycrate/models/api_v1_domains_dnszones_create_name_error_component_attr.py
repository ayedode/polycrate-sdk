from typing import Literal

ApiV1DomainsDnszonesCreateNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DNSZONES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_domains_dnszones_create_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesCreateNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
