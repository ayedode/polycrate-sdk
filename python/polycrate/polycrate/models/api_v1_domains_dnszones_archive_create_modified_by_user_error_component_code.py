from typing import Literal

ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_dnszones_archive_create_modified_by_user_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateModifiedByUserErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
