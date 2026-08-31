from typing import Literal

ApiV1ConditionsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_CONDITIONS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_conditions_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
