from typing import Literal

ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_dnszones_rectify_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
