from typing import Literal

ApiV1ProvidersArchiveCreatePhoneErrorComponentAttr = Literal["phone"]

API_V1_PROVIDERS_ARCHIVE_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreatePhoneErrorComponentAttr
] = {
    "phone",
}


def check_api_v1_providers_archive_create_phone_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreatePhoneErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_PHONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
