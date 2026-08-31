from typing import Literal

ApiV1DomainsDnszonesRectifyCreateNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_domains_dnszones_rectify_create_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
