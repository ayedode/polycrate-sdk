from typing import Literal

ApiV1CredentialsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_credentials_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
