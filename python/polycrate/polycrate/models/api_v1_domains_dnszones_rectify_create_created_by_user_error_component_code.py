from typing import Literal

ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_dnszones_rectify_create_created_by_user_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
