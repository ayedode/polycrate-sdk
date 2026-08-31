from typing import Literal

ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_notes_rescan_provider_status_create_organization_id_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
