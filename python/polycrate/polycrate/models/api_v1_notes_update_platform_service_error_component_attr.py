from typing import Literal

ApiV1NotesUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_NOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_notes_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1NotesUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
