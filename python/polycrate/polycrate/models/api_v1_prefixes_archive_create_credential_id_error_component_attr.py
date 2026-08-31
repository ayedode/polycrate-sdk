from typing import Literal

ApiV1PrefixesArchiveCreateCredentialIdErrorComponentAttr = Literal["credential_id"]

API_V1_PREFIXES_ARCHIVE_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesArchiveCreateCredentialIdErrorComponentAttr
] = {
    "credential_id",
}


def check_api_v1_prefixes_archive_create_credential_id_error_component_attr(
    value: str,
) -> ApiV1PrefixesArchiveCreateCredentialIdErrorComponentAttr:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
