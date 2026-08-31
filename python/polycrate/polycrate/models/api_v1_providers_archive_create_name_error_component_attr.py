from typing import Literal

ApiV1ProvidersArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_PROVIDERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_providers_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreateNameErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
