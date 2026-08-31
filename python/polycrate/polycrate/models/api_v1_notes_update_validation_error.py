from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notes_update_additional_recipients_error_component import (
        ApiV1NotesUpdateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_notes_update_annotations_error_component import ApiV1NotesUpdateAnnotationsErrorComponent
    from ..models.api_v1_notes_update_archived_at_error_component import ApiV1NotesUpdateArchivedAtErrorComponent
    from ..models.api_v1_notes_update_archived_error_component import ApiV1NotesUpdateArchivedErrorComponent
    from ..models.api_v1_notes_update_archived_reason_error_component import (
        ApiV1NotesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notes_update_assigned_to_ids_error_component import ApiV1NotesUpdateAssignedToIdsErrorComponent
    from ..models.api_v1_notes_update_assigned_to_ids_index_error_component import (
        ApiV1NotesUpdateAssignedToIdsINDEXErrorComponent,
    )
    from ..models.api_v1_notes_update_content_error_component import ApiV1NotesUpdateContentErrorComponent
    from ..models.api_v1_notes_update_credential_id_error_component import ApiV1NotesUpdateCredentialIdErrorComponent
    from ..models.api_v1_notes_update_criticality_error_component import ApiV1NotesUpdateCriticalityErrorComponent
    from ..models.api_v1_notes_update_debug_mode_error_component import ApiV1NotesUpdateDebugModeErrorComponent
    from ..models.api_v1_notes_update_display_name_error_component import ApiV1NotesUpdateDisplayNameErrorComponent
    from ..models.api_v1_notes_update_kind_error_component import ApiV1NotesUpdateKindErrorComponent
    from ..models.api_v1_notes_update_labels_error_component import ApiV1NotesUpdateLabelsErrorComponent
    from ..models.api_v1_notes_update_meeting_duration_minutes_error_component import (
        ApiV1NotesUpdateMeetingDurationMinutesErrorComponent,
    )
    from ..models.api_v1_notes_update_name_error_component import ApiV1NotesUpdateNameErrorComponent
    from ..models.api_v1_notes_update_non_field_errors_error_component import (
        ApiV1NotesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notes_update_organization_id_error_component import (
        ApiV1NotesUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_notes_update_parent_note_id_error_component import ApiV1NotesUpdateParentNoteIdErrorComponent
    from ..models.api_v1_notes_update_platform_service_error_component import (
        ApiV1NotesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notes_update_project_id_error_component import ApiV1NotesUpdateProjectIdErrorComponent
    from ..models.api_v1_notes_update_provider_error_component import ApiV1NotesUpdateProviderErrorComponent
    from ..models.api_v1_notes_update_provider_id_error_component import ApiV1NotesUpdateProviderIdErrorComponent
    from ..models.api_v1_notes_update_provider_reference_error_component import (
        ApiV1NotesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notes_update_reconciliation_enabled_error_component import (
        ApiV1NotesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notes_update_remind_at_error_component import ApiV1NotesUpdateRemindAtErrorComponent
    from ..models.api_v1_notes_update_resolved_error_component import ApiV1NotesUpdateResolvedErrorComponent
    from ..models.api_v1_notes_update_sla_availability_error_component import (
        ApiV1NotesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_update_sla_target_error_component import ApiV1NotesUpdateSlaTargetErrorComponent
    from ..models.api_v1_notes_update_slo_availability_error_component import (
        ApiV1NotesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_update_slo_target_error_component import ApiV1NotesUpdateSloTargetErrorComponent
    from ..models.api_v1_notes_update_structured_content_error_component import (
        ApiV1NotesUpdateStructuredContentErrorComponent,
    )
    from ..models.api_v1_notes_update_target_availability_error_component import (
        ApiV1NotesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_update_time_tracked_hours_error_component import (
        ApiV1NotesUpdateTimeTrackedHoursErrorComponent,
    )
    from ..models.api_v1_notes_update_tolerations_error_component import ApiV1NotesUpdateTolerationsErrorComponent
    from ..models.api_v1_notes_update_tracked_at_error_component import ApiV1NotesUpdateTrackedAtErrorComponent
    from ..models.api_v1_notes_update_vydeo_enabled_error_component import ApiV1NotesUpdateVydeoEnabledErrorComponent
    from ..models.api_v1_notes_update_workspace_id_error_component import ApiV1NotesUpdateWorkspaceIdErrorComponent


T = TypeVar("T", bound="ApiV1NotesUpdateValidationError")


@_attrs_define
class ApiV1NotesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotesUpdateAdditionalRecipientsErrorComponent | ApiV1NotesUpdateAnnotationsErrorComponent |
            ApiV1NotesUpdateArchivedAtErrorComponent | ApiV1NotesUpdateArchivedErrorComponent |
            ApiV1NotesUpdateArchivedReasonErrorComponent | ApiV1NotesUpdateAssignedToIdsErrorComponent |
            ApiV1NotesUpdateAssignedToIdsINDEXErrorComponent | ApiV1NotesUpdateContentErrorComponent |
            ApiV1NotesUpdateCredentialIdErrorComponent | ApiV1NotesUpdateCriticalityErrorComponent |
            ApiV1NotesUpdateDebugModeErrorComponent | ApiV1NotesUpdateDisplayNameErrorComponent |
            ApiV1NotesUpdateKindErrorComponent | ApiV1NotesUpdateLabelsErrorComponent |
            ApiV1NotesUpdateMeetingDurationMinutesErrorComponent | ApiV1NotesUpdateNameErrorComponent |
            ApiV1NotesUpdateNonFieldErrorsErrorComponent | ApiV1NotesUpdateOrganizationIdErrorComponent |
            ApiV1NotesUpdateParentNoteIdErrorComponent | ApiV1NotesUpdatePlatformServiceErrorComponent |
            ApiV1NotesUpdateProjectIdErrorComponent | ApiV1NotesUpdateProviderErrorComponent |
            ApiV1NotesUpdateProviderIdErrorComponent | ApiV1NotesUpdateProviderReferenceErrorComponent |
            ApiV1NotesUpdateReconciliationEnabledErrorComponent | ApiV1NotesUpdateRemindAtErrorComponent |
            ApiV1NotesUpdateResolvedErrorComponent | ApiV1NotesUpdateSlaAvailabilityErrorComponent |
            ApiV1NotesUpdateSlaTargetErrorComponent | ApiV1NotesUpdateSloAvailabilityErrorComponent |
            ApiV1NotesUpdateSloTargetErrorComponent | ApiV1NotesUpdateStructuredContentErrorComponent |
            ApiV1NotesUpdateTargetAvailabilityErrorComponent | ApiV1NotesUpdateTimeTrackedHoursErrorComponent |
            ApiV1NotesUpdateTolerationsErrorComponent | ApiV1NotesUpdateTrackedAtErrorComponent |
            ApiV1NotesUpdateVydeoEnabledErrorComponent | ApiV1NotesUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotesUpdateAdditionalRecipientsErrorComponent
        | ApiV1NotesUpdateAnnotationsErrorComponent
        | ApiV1NotesUpdateArchivedAtErrorComponent
        | ApiV1NotesUpdateArchivedErrorComponent
        | ApiV1NotesUpdateArchivedReasonErrorComponent
        | ApiV1NotesUpdateAssignedToIdsErrorComponent
        | ApiV1NotesUpdateAssignedToIdsINDEXErrorComponent
        | ApiV1NotesUpdateContentErrorComponent
        | ApiV1NotesUpdateCredentialIdErrorComponent
        | ApiV1NotesUpdateCriticalityErrorComponent
        | ApiV1NotesUpdateDebugModeErrorComponent
        | ApiV1NotesUpdateDisplayNameErrorComponent
        | ApiV1NotesUpdateKindErrorComponent
        | ApiV1NotesUpdateLabelsErrorComponent
        | ApiV1NotesUpdateMeetingDurationMinutesErrorComponent
        | ApiV1NotesUpdateNameErrorComponent
        | ApiV1NotesUpdateNonFieldErrorsErrorComponent
        | ApiV1NotesUpdateOrganizationIdErrorComponent
        | ApiV1NotesUpdateParentNoteIdErrorComponent
        | ApiV1NotesUpdatePlatformServiceErrorComponent
        | ApiV1NotesUpdateProjectIdErrorComponent
        | ApiV1NotesUpdateProviderErrorComponent
        | ApiV1NotesUpdateProviderIdErrorComponent
        | ApiV1NotesUpdateProviderReferenceErrorComponent
        | ApiV1NotesUpdateReconciliationEnabledErrorComponent
        | ApiV1NotesUpdateRemindAtErrorComponent
        | ApiV1NotesUpdateResolvedErrorComponent
        | ApiV1NotesUpdateSlaAvailabilityErrorComponent
        | ApiV1NotesUpdateSlaTargetErrorComponent
        | ApiV1NotesUpdateSloAvailabilityErrorComponent
        | ApiV1NotesUpdateSloTargetErrorComponent
        | ApiV1NotesUpdateStructuredContentErrorComponent
        | ApiV1NotesUpdateTargetAvailabilityErrorComponent
        | ApiV1NotesUpdateTimeTrackedHoursErrorComponent
        | ApiV1NotesUpdateTolerationsErrorComponent
        | ApiV1NotesUpdateTrackedAtErrorComponent
        | ApiV1NotesUpdateVydeoEnabledErrorComponent
        | ApiV1NotesUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notes_update_additional_recipients_error_component import (
            ApiV1NotesUpdateAdditionalRecipientsErrorComponent,
        )
        from ..models.api_v1_notes_update_annotations_error_component import ApiV1NotesUpdateAnnotationsErrorComponent
        from ..models.api_v1_notes_update_archived_at_error_component import ApiV1NotesUpdateArchivedAtErrorComponent
        from ..models.api_v1_notes_update_archived_error_component import ApiV1NotesUpdateArchivedErrorComponent
        from ..models.api_v1_notes_update_archived_reason_error_component import (
            ApiV1NotesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_notes_update_assigned_to_ids_error_component import (
            ApiV1NotesUpdateAssignedToIdsErrorComponent,
        )
        from ..models.api_v1_notes_update_assigned_to_ids_index_error_component import (
            ApiV1NotesUpdateAssignedToIdsINDEXErrorComponent,
        )
        from ..models.api_v1_notes_update_content_error_component import ApiV1NotesUpdateContentErrorComponent
        from ..models.api_v1_notes_update_credential_id_error_component import (
            ApiV1NotesUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_notes_update_criticality_error_component import ApiV1NotesUpdateCriticalityErrorComponent
        from ..models.api_v1_notes_update_debug_mode_error_component import ApiV1NotesUpdateDebugModeErrorComponent
        from ..models.api_v1_notes_update_display_name_error_component import ApiV1NotesUpdateDisplayNameErrorComponent
        from ..models.api_v1_notes_update_kind_error_component import ApiV1NotesUpdateKindErrorComponent
        from ..models.api_v1_notes_update_labels_error_component import ApiV1NotesUpdateLabelsErrorComponent
        from ..models.api_v1_notes_update_name_error_component import ApiV1NotesUpdateNameErrorComponent
        from ..models.api_v1_notes_update_non_field_errors_error_component import (
            ApiV1NotesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_notes_update_organization_id_error_component import (
            ApiV1NotesUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_notes_update_parent_note_id_error_component import (
            ApiV1NotesUpdateParentNoteIdErrorComponent,
        )
        from ..models.api_v1_notes_update_platform_service_error_component import (
            ApiV1NotesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_notes_update_project_id_error_component import ApiV1NotesUpdateProjectIdErrorComponent
        from ..models.api_v1_notes_update_provider_error_component import ApiV1NotesUpdateProviderErrorComponent
        from ..models.api_v1_notes_update_provider_id_error_component import ApiV1NotesUpdateProviderIdErrorComponent
        from ..models.api_v1_notes_update_provider_reference_error_component import (
            ApiV1NotesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_notes_update_reconciliation_enabled_error_component import (
            ApiV1NotesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_notes_update_remind_at_error_component import ApiV1NotesUpdateRemindAtErrorComponent
        from ..models.api_v1_notes_update_resolved_error_component import ApiV1NotesUpdateResolvedErrorComponent
        from ..models.api_v1_notes_update_sla_availability_error_component import (
            ApiV1NotesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_notes_update_sla_target_error_component import ApiV1NotesUpdateSlaTargetErrorComponent
        from ..models.api_v1_notes_update_slo_availability_error_component import (
            ApiV1NotesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_notes_update_slo_target_error_component import ApiV1NotesUpdateSloTargetErrorComponent
        from ..models.api_v1_notes_update_structured_content_error_component import (
            ApiV1NotesUpdateStructuredContentErrorComponent,
        )
        from ..models.api_v1_notes_update_target_availability_error_component import (
            ApiV1NotesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_notes_update_time_tracked_hours_error_component import (
            ApiV1NotesUpdateTimeTrackedHoursErrorComponent,
        )
        from ..models.api_v1_notes_update_tolerations_error_component import ApiV1NotesUpdateTolerationsErrorComponent
        from ..models.api_v1_notes_update_tracked_at_error_component import ApiV1NotesUpdateTrackedAtErrorComponent
        from ..models.api_v1_notes_update_vydeo_enabled_error_component import (
            ApiV1NotesUpdateVydeoEnabledErrorComponent,
        )
        from ..models.api_v1_notes_update_workspace_id_error_component import ApiV1NotesUpdateWorkspaceIdErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateStructuredContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateParentNoteIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateTimeTrackedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateAssignedToIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateAssignedToIdsINDEXErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateRemindAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateTrackedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateVydeoEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesUpdateAdditionalRecipientsErrorComponent):
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
        from ..models.api_v1_notes_update_additional_recipients_error_component import (
            ApiV1NotesUpdateAdditionalRecipientsErrorComponent,
        )
        from ..models.api_v1_notes_update_annotations_error_component import ApiV1NotesUpdateAnnotationsErrorComponent
        from ..models.api_v1_notes_update_archived_at_error_component import ApiV1NotesUpdateArchivedAtErrorComponent
        from ..models.api_v1_notes_update_archived_error_component import ApiV1NotesUpdateArchivedErrorComponent
        from ..models.api_v1_notes_update_archived_reason_error_component import (
            ApiV1NotesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_notes_update_assigned_to_ids_error_component import (
            ApiV1NotesUpdateAssignedToIdsErrorComponent,
        )
        from ..models.api_v1_notes_update_assigned_to_ids_index_error_component import (
            ApiV1NotesUpdateAssignedToIdsINDEXErrorComponent,
        )
        from ..models.api_v1_notes_update_content_error_component import ApiV1NotesUpdateContentErrorComponent
        from ..models.api_v1_notes_update_credential_id_error_component import (
            ApiV1NotesUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_notes_update_criticality_error_component import ApiV1NotesUpdateCriticalityErrorComponent
        from ..models.api_v1_notes_update_debug_mode_error_component import ApiV1NotesUpdateDebugModeErrorComponent
        from ..models.api_v1_notes_update_display_name_error_component import ApiV1NotesUpdateDisplayNameErrorComponent
        from ..models.api_v1_notes_update_kind_error_component import ApiV1NotesUpdateKindErrorComponent
        from ..models.api_v1_notes_update_labels_error_component import ApiV1NotesUpdateLabelsErrorComponent
        from ..models.api_v1_notes_update_meeting_duration_minutes_error_component import (
            ApiV1NotesUpdateMeetingDurationMinutesErrorComponent,
        )
        from ..models.api_v1_notes_update_name_error_component import ApiV1NotesUpdateNameErrorComponent
        from ..models.api_v1_notes_update_non_field_errors_error_component import (
            ApiV1NotesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_notes_update_organization_id_error_component import (
            ApiV1NotesUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_notes_update_parent_note_id_error_component import (
            ApiV1NotesUpdateParentNoteIdErrorComponent,
        )
        from ..models.api_v1_notes_update_platform_service_error_component import (
            ApiV1NotesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_notes_update_project_id_error_component import ApiV1NotesUpdateProjectIdErrorComponent
        from ..models.api_v1_notes_update_provider_error_component import ApiV1NotesUpdateProviderErrorComponent
        from ..models.api_v1_notes_update_provider_id_error_component import ApiV1NotesUpdateProviderIdErrorComponent
        from ..models.api_v1_notes_update_provider_reference_error_component import (
            ApiV1NotesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_notes_update_reconciliation_enabled_error_component import (
            ApiV1NotesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_notes_update_remind_at_error_component import ApiV1NotesUpdateRemindAtErrorComponent
        from ..models.api_v1_notes_update_resolved_error_component import ApiV1NotesUpdateResolvedErrorComponent
        from ..models.api_v1_notes_update_sla_availability_error_component import (
            ApiV1NotesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_notes_update_sla_target_error_component import ApiV1NotesUpdateSlaTargetErrorComponent
        from ..models.api_v1_notes_update_slo_availability_error_component import (
            ApiV1NotesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_notes_update_slo_target_error_component import ApiV1NotesUpdateSloTargetErrorComponent
        from ..models.api_v1_notes_update_structured_content_error_component import (
            ApiV1NotesUpdateStructuredContentErrorComponent,
        )
        from ..models.api_v1_notes_update_target_availability_error_component import (
            ApiV1NotesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_notes_update_time_tracked_hours_error_component import (
            ApiV1NotesUpdateTimeTrackedHoursErrorComponent,
        )
        from ..models.api_v1_notes_update_tolerations_error_component import ApiV1NotesUpdateTolerationsErrorComponent
        from ..models.api_v1_notes_update_tracked_at_error_component import ApiV1NotesUpdateTrackedAtErrorComponent
        from ..models.api_v1_notes_update_vydeo_enabled_error_component import (
            ApiV1NotesUpdateVydeoEnabledErrorComponent,
        )
        from ..models.api_v1_notes_update_workspace_id_error_component import ApiV1NotesUpdateWorkspaceIdErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotesUpdateAdditionalRecipientsErrorComponent
                | ApiV1NotesUpdateAnnotationsErrorComponent
                | ApiV1NotesUpdateArchivedAtErrorComponent
                | ApiV1NotesUpdateArchivedErrorComponent
                | ApiV1NotesUpdateArchivedReasonErrorComponent
                | ApiV1NotesUpdateAssignedToIdsErrorComponent
                | ApiV1NotesUpdateAssignedToIdsINDEXErrorComponent
                | ApiV1NotesUpdateContentErrorComponent
                | ApiV1NotesUpdateCredentialIdErrorComponent
                | ApiV1NotesUpdateCriticalityErrorComponent
                | ApiV1NotesUpdateDebugModeErrorComponent
                | ApiV1NotesUpdateDisplayNameErrorComponent
                | ApiV1NotesUpdateKindErrorComponent
                | ApiV1NotesUpdateLabelsErrorComponent
                | ApiV1NotesUpdateMeetingDurationMinutesErrorComponent
                | ApiV1NotesUpdateNameErrorComponent
                | ApiV1NotesUpdateNonFieldErrorsErrorComponent
                | ApiV1NotesUpdateOrganizationIdErrorComponent
                | ApiV1NotesUpdateParentNoteIdErrorComponent
                | ApiV1NotesUpdatePlatformServiceErrorComponent
                | ApiV1NotesUpdateProjectIdErrorComponent
                | ApiV1NotesUpdateProviderErrorComponent
                | ApiV1NotesUpdateProviderIdErrorComponent
                | ApiV1NotesUpdateProviderReferenceErrorComponent
                | ApiV1NotesUpdateReconciliationEnabledErrorComponent
                | ApiV1NotesUpdateRemindAtErrorComponent
                | ApiV1NotesUpdateResolvedErrorComponent
                | ApiV1NotesUpdateSlaAvailabilityErrorComponent
                | ApiV1NotesUpdateSlaTargetErrorComponent
                | ApiV1NotesUpdateSloAvailabilityErrorComponent
                | ApiV1NotesUpdateSloTargetErrorComponent
                | ApiV1NotesUpdateStructuredContentErrorComponent
                | ApiV1NotesUpdateTargetAvailabilityErrorComponent
                | ApiV1NotesUpdateTimeTrackedHoursErrorComponent
                | ApiV1NotesUpdateTolerationsErrorComponent
                | ApiV1NotesUpdateTrackedAtErrorComponent
                | ApiV1NotesUpdateVydeoEnabledErrorComponent
                | ApiV1NotesUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_0 = (
                        ApiV1NotesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_1 = ApiV1NotesUpdateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_2 = (
                        ApiV1NotesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_3 = ApiV1NotesUpdateLabelsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_4 = (
                        ApiV1NotesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_5 = (
                        ApiV1NotesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_6 = (
                        ApiV1NotesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_7 = (
                        ApiV1NotesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_8 = (
                        ApiV1NotesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_9 = (
                        ApiV1NotesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_10 = (
                        ApiV1NotesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_11 = ApiV1NotesUpdateKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_12 = (
                        ApiV1NotesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_13 = (
                        ApiV1NotesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_14 = (
                        ApiV1NotesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_15 = (
                        ApiV1NotesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_16 = (
                        ApiV1NotesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_17 = (
                        ApiV1NotesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_18 = (
                        ApiV1NotesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_19 = (
                        ApiV1NotesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_20 = (
                        ApiV1NotesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_21 = (
                        ApiV1NotesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_22 = (
                        ApiV1NotesUpdateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_23 = (
                        ApiV1NotesUpdateStructuredContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_24 = (
                        ApiV1NotesUpdateResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_25 = (
                        ApiV1NotesUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_26 = (
                        ApiV1NotesUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_27 = (
                        ApiV1NotesUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_28 = (
                        ApiV1NotesUpdateParentNoteIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_29 = (
                        ApiV1NotesUpdateTimeTrackedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_30 = (
                        ApiV1NotesUpdateAssignedToIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_31 = (
                        ApiV1NotesUpdateAssignedToIdsINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_32 = (
                        ApiV1NotesUpdateRemindAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_33 = (
                        ApiV1NotesUpdateTrackedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_34 = (
                        ApiV1NotesUpdateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_35 = (
                        ApiV1NotesUpdateVydeoEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_update_error_type_36 = (
                        ApiV1NotesUpdateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notes_update_error_type_37 = (
                    ApiV1NotesUpdateMeetingDurationMinutesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notes_update_error_type_37

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notes_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notes_update_validation_error.additional_properties = d
        return api_v1_notes_update_validation_error

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
