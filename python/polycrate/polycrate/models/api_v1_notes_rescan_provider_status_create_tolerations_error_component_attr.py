from typing import Literal

ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_notes_rescan_provider_status_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
