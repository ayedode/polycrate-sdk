from typing import Literal

ApiV1ProvidersArchiveCreateLegalNameErrorComponentAttr = Literal["legal_name"]

API_V1_PROVIDERS_ARCHIVE_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreateLegalNameErrorComponentAttr
] = {
    "legal_name",
}


def check_api_v1_providers_archive_create_legal_name_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreateLegalNameErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
