from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notes_partial_update_additional_recipients_error_component import (
        ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_annotations_error_component import (
        ApiV1NotesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_archived_at_error_component import (
        ApiV1NotesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_archived_error_component import (
        ApiV1NotesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_archived_reason_error_component import (
        ApiV1NotesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_assigned_to_ids_error_component import (
        ApiV1NotesPartialUpdateAssignedToIdsErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_assigned_to_ids_index_error_component import (
        ApiV1NotesPartialUpdateAssignedToIdsINDEXErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_content_error_component import (
        ApiV1NotesPartialUpdateContentErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_credential_id_error_component import (
        ApiV1NotesPartialUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_criticality_error_component import (
        ApiV1NotesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_debug_mode_error_component import (
        ApiV1NotesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_display_name_error_component import (
        ApiV1NotesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_kind_error_component import ApiV1NotesPartialUpdateKindErrorComponent
    from ..models.api_v1_notes_partial_update_labels_error_component import ApiV1NotesPartialUpdateLabelsErrorComponent
    from ..models.api_v1_notes_partial_update_meeting_duration_minutes_error_component import (
        ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_name_error_component import ApiV1NotesPartialUpdateNameErrorComponent
    from ..models.api_v1_notes_partial_update_non_field_errors_error_component import (
        ApiV1NotesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_organization_id_error_component import (
        ApiV1NotesPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_parent_note_id_error_component import (
        ApiV1NotesPartialUpdateParentNoteIdErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_platform_service_error_component import (
        ApiV1NotesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_project_id_error_component import (
        ApiV1NotesPartialUpdateProjectIdErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_provider_error_component import (
        ApiV1NotesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_provider_id_error_component import (
        ApiV1NotesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_provider_reference_error_component import (
        ApiV1NotesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_reconciliation_enabled_error_component import (
        ApiV1NotesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_remind_at_error_component import (
        ApiV1NotesPartialUpdateRemindAtErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_resolved_error_component import (
        ApiV1NotesPartialUpdateResolvedErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_sla_availability_error_component import (
        ApiV1NotesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_sla_target_error_component import (
        ApiV1NotesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_slo_availability_error_component import (
        ApiV1NotesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_slo_target_error_component import (
        ApiV1NotesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_structured_content_error_component import (
        ApiV1NotesPartialUpdateStructuredContentErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_target_availability_error_component import (
        ApiV1NotesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_time_tracked_hours_error_component import (
        ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_tolerations_error_component import (
        ApiV1NotesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_tracked_at_error_component import (
        ApiV1NotesPartialUpdateTrackedAtErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_vydeo_enabled_error_component import (
        ApiV1NotesPartialUpdateVydeoEnabledErrorComponent,
    )
    from ..models.api_v1_notes_partial_update_workspace_id_error_component import (
        ApiV1NotesPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotesPartialUpdateValidationError")


@_attrs_define
class ApiV1NotesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponent |
            ApiV1NotesPartialUpdateAnnotationsErrorComponent | ApiV1NotesPartialUpdateArchivedAtErrorComponent |
            ApiV1NotesPartialUpdateArchivedErrorComponent | ApiV1NotesPartialUpdateArchivedReasonErrorComponent |
            ApiV1NotesPartialUpdateAssignedToIdsErrorComponent | ApiV1NotesPartialUpdateAssignedToIdsINDEXErrorComponent |
            ApiV1NotesPartialUpdateContentErrorComponent | ApiV1NotesPartialUpdateCredentialIdErrorComponent |
            ApiV1NotesPartialUpdateCriticalityErrorComponent | ApiV1NotesPartialUpdateDebugModeErrorComponent |
            ApiV1NotesPartialUpdateDisplayNameErrorComponent | ApiV1NotesPartialUpdateKindErrorComponent |
            ApiV1NotesPartialUpdateLabelsErrorComponent | ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponent |
            ApiV1NotesPartialUpdateNameErrorComponent | ApiV1NotesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1NotesPartialUpdateOrganizationIdErrorComponent | ApiV1NotesPartialUpdateParentNoteIdErrorComponent |
            ApiV1NotesPartialUpdatePlatformServiceErrorComponent | ApiV1NotesPartialUpdateProjectIdErrorComponent |
            ApiV1NotesPartialUpdateProviderErrorComponent | ApiV1NotesPartialUpdateProviderIdErrorComponent |
            ApiV1NotesPartialUpdateProviderReferenceErrorComponent |
            ApiV1NotesPartialUpdateReconciliationEnabledErrorComponent | ApiV1NotesPartialUpdateRemindAtErrorComponent |
            ApiV1NotesPartialUpdateResolvedErrorComponent | ApiV1NotesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1NotesPartialUpdateSlaTargetErrorComponent | ApiV1NotesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1NotesPartialUpdateSloTargetErrorComponent | ApiV1NotesPartialUpdateStructuredContentErrorComponent |
            ApiV1NotesPartialUpdateTargetAvailabilityErrorComponent | ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponent
            | ApiV1NotesPartialUpdateTolerationsErrorComponent | ApiV1NotesPartialUpdateTrackedAtErrorComponent |
            ApiV1NotesPartialUpdateVydeoEnabledErrorComponent | ApiV1NotesPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponent
        | ApiV1NotesPartialUpdateAnnotationsErrorComponent
        | ApiV1NotesPartialUpdateArchivedAtErrorComponent
        | ApiV1NotesPartialUpdateArchivedErrorComponent
        | ApiV1NotesPartialUpdateArchivedReasonErrorComponent
        | ApiV1NotesPartialUpdateAssignedToIdsErrorComponent
        | ApiV1NotesPartialUpdateAssignedToIdsINDEXErrorComponent
        | ApiV1NotesPartialUpdateContentErrorComponent
        | ApiV1NotesPartialUpdateCredentialIdErrorComponent
        | ApiV1NotesPartialUpdateCriticalityErrorComponent
        | ApiV1NotesPartialUpdateDebugModeErrorComponent
        | ApiV1NotesPartialUpdateDisplayNameErrorComponent
        | ApiV1NotesPartialUpdateKindErrorComponent
        | ApiV1NotesPartialUpdateLabelsErrorComponent
        | ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponent
        | ApiV1NotesPartialUpdateNameErrorComponent
        | ApiV1NotesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1NotesPartialUpdateOrganizationIdErrorComponent
        | ApiV1NotesPartialUpdateParentNoteIdErrorComponent
        | ApiV1NotesPartialUpdatePlatformServiceErrorComponent
        | ApiV1NotesPartialUpdateProjectIdErrorComponent
        | ApiV1NotesPartialUpdateProviderErrorComponent
        | ApiV1NotesPartialUpdateProviderIdErrorComponent
        | ApiV1NotesPartialUpdateProviderReferenceErrorComponent
        | ApiV1NotesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1NotesPartialUpdateRemindAtErrorComponent
        | ApiV1NotesPartialUpdateResolvedErrorComponent
        | ApiV1NotesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1NotesPartialUpdateSlaTargetErrorComponent
        | ApiV1NotesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1NotesPartialUpdateSloTargetErrorComponent
        | ApiV1NotesPartialUpdateStructuredContentErrorComponent
        | ApiV1NotesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponent
        | ApiV1NotesPartialUpdateTolerationsErrorComponent
        | ApiV1NotesPartialUpdateTrackedAtErrorComponent
        | ApiV1NotesPartialUpdateVydeoEnabledErrorComponent
        | ApiV1NotesPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notes_partial_update_additional_recipients_error_component import (
            ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_annotations_error_component import (
            ApiV1NotesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_archived_at_error_component import (
            ApiV1NotesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_archived_error_component import (
            ApiV1NotesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_archived_reason_error_component import (
            ApiV1NotesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_assigned_to_ids_error_component import (
            ApiV1NotesPartialUpdateAssignedToIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_assigned_to_ids_index_error_component import (
            ApiV1NotesPartialUpdateAssignedToIdsINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_content_error_component import (
            ApiV1NotesPartialUpdateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_credential_id_error_component import (
            ApiV1NotesPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_criticality_error_component import (
            ApiV1NotesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_debug_mode_error_component import (
            ApiV1NotesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_display_name_error_component import (
            ApiV1NotesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_kind_error_component import (
            ApiV1NotesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_labels_error_component import (
            ApiV1NotesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_name_error_component import (
            ApiV1NotesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_non_field_errors_error_component import (
            ApiV1NotesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_organization_id_error_component import (
            ApiV1NotesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_parent_note_id_error_component import (
            ApiV1NotesPartialUpdateParentNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_platform_service_error_component import (
            ApiV1NotesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_project_id_error_component import (
            ApiV1NotesPartialUpdateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_provider_error_component import (
            ApiV1NotesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_provider_id_error_component import (
            ApiV1NotesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_provider_reference_error_component import (
            ApiV1NotesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_reconciliation_enabled_error_component import (
            ApiV1NotesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_remind_at_error_component import (
            ApiV1NotesPartialUpdateRemindAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_resolved_error_component import (
            ApiV1NotesPartialUpdateResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_sla_availability_error_component import (
            ApiV1NotesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_sla_target_error_component import (
            ApiV1NotesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_slo_availability_error_component import (
            ApiV1NotesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_slo_target_error_component import (
            ApiV1NotesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_structured_content_error_component import (
            ApiV1NotesPartialUpdateStructuredContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_target_availability_error_component import (
            ApiV1NotesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_time_tracked_hours_error_component import (
            ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_tolerations_error_component import (
            ApiV1NotesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_tracked_at_error_component import (
            ApiV1NotesPartialUpdateTrackedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_vydeo_enabled_error_component import (
            ApiV1NotesPartialUpdateVydeoEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_workspace_id_error_component import (
            ApiV1NotesPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateStructuredContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateParentNoteIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateAssignedToIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateAssignedToIdsINDEXErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateRemindAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateTrackedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateVydeoEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_notes_partial_update_additional_recipients_error_component import (
            ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_annotations_error_component import (
            ApiV1NotesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_archived_at_error_component import (
            ApiV1NotesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_archived_error_component import (
            ApiV1NotesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_archived_reason_error_component import (
            ApiV1NotesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_assigned_to_ids_error_component import (
            ApiV1NotesPartialUpdateAssignedToIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_assigned_to_ids_index_error_component import (
            ApiV1NotesPartialUpdateAssignedToIdsINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_content_error_component import (
            ApiV1NotesPartialUpdateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_credential_id_error_component import (
            ApiV1NotesPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_criticality_error_component import (
            ApiV1NotesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_debug_mode_error_component import (
            ApiV1NotesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_display_name_error_component import (
            ApiV1NotesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_kind_error_component import (
            ApiV1NotesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_labels_error_component import (
            ApiV1NotesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_meeting_duration_minutes_error_component import (
            ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_name_error_component import (
            ApiV1NotesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_non_field_errors_error_component import (
            ApiV1NotesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_organization_id_error_component import (
            ApiV1NotesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_parent_note_id_error_component import (
            ApiV1NotesPartialUpdateParentNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_platform_service_error_component import (
            ApiV1NotesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_project_id_error_component import (
            ApiV1NotesPartialUpdateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_provider_error_component import (
            ApiV1NotesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_provider_id_error_component import (
            ApiV1NotesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_provider_reference_error_component import (
            ApiV1NotesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_reconciliation_enabled_error_component import (
            ApiV1NotesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_remind_at_error_component import (
            ApiV1NotesPartialUpdateRemindAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_resolved_error_component import (
            ApiV1NotesPartialUpdateResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_sla_availability_error_component import (
            ApiV1NotesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_sla_target_error_component import (
            ApiV1NotesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_slo_availability_error_component import (
            ApiV1NotesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_slo_target_error_component import (
            ApiV1NotesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_structured_content_error_component import (
            ApiV1NotesPartialUpdateStructuredContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_target_availability_error_component import (
            ApiV1NotesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_time_tracked_hours_error_component import (
            ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_tolerations_error_component import (
            ApiV1NotesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_tracked_at_error_component import (
            ApiV1NotesPartialUpdateTrackedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_vydeo_enabled_error_component import (
            ApiV1NotesPartialUpdateVydeoEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_partial_update_workspace_id_error_component import (
            ApiV1NotesPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponent
                | ApiV1NotesPartialUpdateAnnotationsErrorComponent
                | ApiV1NotesPartialUpdateArchivedAtErrorComponent
                | ApiV1NotesPartialUpdateArchivedErrorComponent
                | ApiV1NotesPartialUpdateArchivedReasonErrorComponent
                | ApiV1NotesPartialUpdateAssignedToIdsErrorComponent
                | ApiV1NotesPartialUpdateAssignedToIdsINDEXErrorComponent
                | ApiV1NotesPartialUpdateContentErrorComponent
                | ApiV1NotesPartialUpdateCredentialIdErrorComponent
                | ApiV1NotesPartialUpdateCriticalityErrorComponent
                | ApiV1NotesPartialUpdateDebugModeErrorComponent
                | ApiV1NotesPartialUpdateDisplayNameErrorComponent
                | ApiV1NotesPartialUpdateKindErrorComponent
                | ApiV1NotesPartialUpdateLabelsErrorComponent
                | ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponent
                | ApiV1NotesPartialUpdateNameErrorComponent
                | ApiV1NotesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1NotesPartialUpdateOrganizationIdErrorComponent
                | ApiV1NotesPartialUpdateParentNoteIdErrorComponent
                | ApiV1NotesPartialUpdatePlatformServiceErrorComponent
                | ApiV1NotesPartialUpdateProjectIdErrorComponent
                | ApiV1NotesPartialUpdateProviderErrorComponent
                | ApiV1NotesPartialUpdateProviderIdErrorComponent
                | ApiV1NotesPartialUpdateProviderReferenceErrorComponent
                | ApiV1NotesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1NotesPartialUpdateRemindAtErrorComponent
                | ApiV1NotesPartialUpdateResolvedErrorComponent
                | ApiV1NotesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1NotesPartialUpdateSlaTargetErrorComponent
                | ApiV1NotesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1NotesPartialUpdateSloTargetErrorComponent
                | ApiV1NotesPartialUpdateStructuredContentErrorComponent
                | ApiV1NotesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponent
                | ApiV1NotesPartialUpdateTolerationsErrorComponent
                | ApiV1NotesPartialUpdateTrackedAtErrorComponent
                | ApiV1NotesPartialUpdateVydeoEnabledErrorComponent
                | ApiV1NotesPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_0 = (
                        ApiV1NotesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_1 = (
                        ApiV1NotesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_2 = (
                        ApiV1NotesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_3 = (
                        ApiV1NotesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_4 = (
                        ApiV1NotesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_5 = (
                        ApiV1NotesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_6 = (
                        ApiV1NotesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_7 = (
                        ApiV1NotesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_8 = (
                        ApiV1NotesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_9 = (
                        ApiV1NotesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_10 = (
                        ApiV1NotesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_11 = (
                        ApiV1NotesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_12 = (
                        ApiV1NotesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_13 = (
                        ApiV1NotesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_14 = (
                        ApiV1NotesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_15 = (
                        ApiV1NotesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_16 = (
                        ApiV1NotesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_17 = (
                        ApiV1NotesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_18 = (
                        ApiV1NotesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_19 = (
                        ApiV1NotesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_20 = (
                        ApiV1NotesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_21 = (
                        ApiV1NotesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_22 = (
                        ApiV1NotesPartialUpdateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_23 = (
                        ApiV1NotesPartialUpdateStructuredContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_24 = (
                        ApiV1NotesPartialUpdateResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_25 = (
                        ApiV1NotesPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_26 = (
                        ApiV1NotesPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_27 = (
                        ApiV1NotesPartialUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_28 = (
                        ApiV1NotesPartialUpdateParentNoteIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_29 = (
                        ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_30 = (
                        ApiV1NotesPartialUpdateAssignedToIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_31 = (
                        ApiV1NotesPartialUpdateAssignedToIdsINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_32 = (
                        ApiV1NotesPartialUpdateRemindAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_33 = (
                        ApiV1NotesPartialUpdateTrackedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_34 = (
                        ApiV1NotesPartialUpdateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_35 = (
                        ApiV1NotesPartialUpdateVydeoEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_partial_update_error_type_36 = (
                        ApiV1NotesPartialUpdateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notes_partial_update_error_type_37 = (
                    ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notes_partial_update_error_type_37

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notes_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notes_partial_update_validation_error.additional_properties = d
        return api_v1_notes_partial_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
