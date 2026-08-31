from typing import Literal

ApiV1ConditionsArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CONDITIONS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_conditions_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
