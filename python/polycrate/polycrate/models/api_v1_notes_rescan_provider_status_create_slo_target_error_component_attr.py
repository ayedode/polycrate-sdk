from typing import Literal

ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_notes_rescan_provider_status_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
