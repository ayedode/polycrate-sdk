from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notes_create_additional_recipients_error_component import (
        ApiV1NotesCreateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_notes_create_annotations_error_component import ApiV1NotesCreateAnnotationsErrorComponent
    from ..models.api_v1_notes_create_archived_at_error_component import ApiV1NotesCreateArchivedAtErrorComponent
    from ..models.api_v1_notes_create_archived_error_component import ApiV1NotesCreateArchivedErrorComponent
    from ..models.api_v1_notes_create_archived_reason_error_component import (
        ApiV1NotesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notes_create_assigned_to_ids_error_component import ApiV1NotesCreateAssignedToIdsErrorComponent
    from ..models.api_v1_notes_create_assigned_to_ids_index_error_component import (
        ApiV1NotesCreateAssignedToIdsINDEXErrorComponent,
    )
    from ..models.api_v1_notes_create_content_error_component import ApiV1NotesCreateContentErrorComponent
    from ..models.api_v1_notes_create_credential_id_error_component import ApiV1NotesCreateCredentialIdErrorComponent
    from ..models.api_v1_notes_create_criticality_error_component import ApiV1NotesCreateCriticalityErrorComponent
    from ..models.api_v1_notes_create_debug_mode_error_component import ApiV1NotesCreateDebugModeErrorComponent
    from ..models.api_v1_notes_create_display_name_error_component import ApiV1NotesCreateDisplayNameErrorComponent
    from ..models.api_v1_notes_create_kind_error_component import ApiV1NotesCreateKindErrorComponent
    from ..models.api_v1_notes_create_labels_error_component import ApiV1NotesCreateLabelsErrorComponent
    from ..models.api_v1_notes_create_meeting_duration_minutes_error_component import (
        ApiV1NotesCreateMeetingDurationMinutesErrorComponent,
    )
    from ..models.api_v1_notes_create_name_error_component import ApiV1NotesCreateNameErrorComponent
    from ..models.api_v1_notes_create_non_field_errors_error_component import (
        ApiV1NotesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notes_create_organization_id_error_component import (
        ApiV1NotesCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_notes_create_parent_note_id_error_component import ApiV1NotesCreateParentNoteIdErrorComponent
    from ..models.api_v1_notes_create_platform_service_error_component import (
        ApiV1NotesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notes_create_project_id_error_component import ApiV1NotesCreateProjectIdErrorComponent
    from ..models.api_v1_notes_create_provider_error_component import ApiV1NotesCreateProviderErrorComponent
    from ..models.api_v1_notes_create_provider_id_error_component import ApiV1NotesCreateProviderIdErrorComponent
    from ..models.api_v1_notes_create_provider_reference_error_component import (
        ApiV1NotesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notes_create_reconciliation_enabled_error_component import (
        ApiV1NotesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notes_create_remind_at_error_component import ApiV1NotesCreateRemindAtErrorComponent
    from ..models.api_v1_notes_create_resolved_error_component import ApiV1NotesCreateResolvedErrorComponent
    from ..models.api_v1_notes_create_sla_availability_error_component import (
        ApiV1NotesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_create_sla_target_error_component import ApiV1NotesCreateSlaTargetErrorComponent
    from ..models.api_v1_notes_create_slo_availability_error_component import (
        ApiV1NotesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_create_slo_target_error_component import ApiV1NotesCreateSloTargetErrorComponent
    from ..models.api_v1_notes_create_structured_content_error_component import (
        ApiV1NotesCreateStructuredContentErrorComponent,
    )
    from ..models.api_v1_notes_create_target_availability_error_component import (
        ApiV1NotesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_create_time_tracked_hours_error_component import (
        ApiV1NotesCreateTimeTrackedHoursErrorComponent,
    )
    from ..models.api_v1_notes_create_tolerations_error_component import ApiV1NotesCreateTolerationsErrorComponent
    from ..models.api_v1_notes_create_tracked_at_error_component import ApiV1NotesCreateTrackedAtErrorComponent
    from ..models.api_v1_notes_create_vydeo_enabled_error_component import ApiV1NotesCreateVydeoEnabledErrorComponent
    from ..models.api_v1_notes_create_workspace_id_error_component import ApiV1NotesCreateWorkspaceIdErrorComponent


T = TypeVar("T", bound="ApiV1NotesCreateValidationError")


@_attrs_define
class ApiV1NotesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotesCreateAdditionalRecipientsErrorComponent | ApiV1NotesCreateAnnotationsErrorComponent |
            ApiV1NotesCreateArchivedAtErrorComponent | ApiV1NotesCreateArchivedErrorComponent |
            ApiV1NotesCreateArchivedReasonErrorComponent | ApiV1NotesCreateAssignedToIdsErrorComponent |
            ApiV1NotesCreateAssignedToIdsINDEXErrorComponent | ApiV1NotesCreateContentErrorComponent |
            ApiV1NotesCreateCredentialIdErrorComponent | ApiV1NotesCreateCriticalityErrorComponent |
            ApiV1NotesCreateDebugModeErrorComponent | ApiV1NotesCreateDisplayNameErrorComponent |
            ApiV1NotesCreateKindErrorComponent | ApiV1NotesCreateLabelsErrorComponent |
            ApiV1NotesCreateMeetingDurationMinutesErrorComponent | ApiV1NotesCreateNameErrorComponent |
            ApiV1NotesCreateNonFieldErrorsErrorComponent | ApiV1NotesCreateOrganizationIdErrorComponent |
            ApiV1NotesCreateParentNoteIdErrorComponent | ApiV1NotesCreatePlatformServiceErrorComponent |
            ApiV1NotesCreateProjectIdErrorComponent | ApiV1NotesCreateProviderErrorComponent |
            ApiV1NotesCreateProviderIdErrorComponent | ApiV1NotesCreateProviderReferenceErrorComponent |
            ApiV1NotesCreateReconciliationEnabledErrorComponent | ApiV1NotesCreateRemindAtErrorComponent |
            ApiV1NotesCreateResolvedErrorComponent | ApiV1NotesCreateSlaAvailabilityErrorComponent |
            ApiV1NotesCreateSlaTargetErrorComponent | ApiV1NotesCreateSloAvailabilityErrorComponent |
            ApiV1NotesCreateSloTargetErrorComponent | ApiV1NotesCreateStructuredContentErrorComponent |
            ApiV1NotesCreateTargetAvailabilityErrorComponent | ApiV1NotesCreateTimeTrackedHoursErrorComponent |
            ApiV1NotesCreateTolerationsErrorComponent | ApiV1NotesCreateTrackedAtErrorComponent |
            ApiV1NotesCreateVydeoEnabledErrorComponent | ApiV1NotesCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotesCreateAdditionalRecipientsErrorComponent
        | ApiV1NotesCreateAnnotationsErrorComponent
        | ApiV1NotesCreateArchivedAtErrorComponent
        | ApiV1NotesCreateArchivedErrorComponent
        | ApiV1NotesCreateArchivedReasonErrorComponent
        | ApiV1NotesCreateAssignedToIdsErrorComponent
        | ApiV1NotesCreateAssignedToIdsINDEXErrorComponent
        | ApiV1NotesCreateContentErrorComponent
        | ApiV1NotesCreateCredentialIdErrorComponent
        | ApiV1NotesCreateCriticalityErrorComponent
        | ApiV1NotesCreateDebugModeErrorComponent
        | ApiV1NotesCreateDisplayNameErrorComponent
        | ApiV1NotesCreateKindErrorComponent
        | ApiV1NotesCreateLabelsErrorComponent
        | ApiV1NotesCreateMeetingDurationMinutesErrorComponent
        | ApiV1NotesCreateNameErrorComponent
        | ApiV1NotesCreateNonFieldErrorsErrorComponent
        | ApiV1NotesCreateOrganizationIdErrorComponent
        | ApiV1NotesCreateParentNoteIdErrorComponent
        | ApiV1NotesCreatePlatformServiceErrorComponent
        | ApiV1NotesCreateProjectIdErrorComponent
        | ApiV1NotesCreateProviderErrorComponent
        | ApiV1NotesCreateProviderIdErrorComponent
        | ApiV1NotesCreateProviderReferenceErrorComponent
        | ApiV1NotesCreateReconciliationEnabledErrorComponent
        | ApiV1NotesCreateRemindAtErrorComponent
        | ApiV1NotesCreateResolvedErrorComponent
        | ApiV1NotesCreateSlaAvailabilityErrorComponent
        | ApiV1NotesCreateSlaTargetErrorComponent
        | ApiV1NotesCreateSloAvailabilityErrorComponent
        | ApiV1NotesCreateSloTargetErrorComponent
        | ApiV1NotesCreateStructuredContentErrorComponent
        | ApiV1NotesCreateTargetAvailabilityErrorComponent
        | ApiV1NotesCreateTimeTrackedHoursErrorComponent
        | ApiV1NotesCreateTolerationsErrorComponent
        | ApiV1NotesCreateTrackedAtErrorComponent
        | ApiV1NotesCreateVydeoEnabledErrorComponent
        | ApiV1NotesCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notes_create_additional_recipients_error_component import (
            ApiV1NotesCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_annotations_error_component import (
            ApiV1NotesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_archived_at_error_component import (
            ApiV1NotesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_archived_error_component import (
            ApiV1NotesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_archived_reason_error_component import (
            ApiV1NotesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_assigned_to_ids_error_component import (
            ApiV1NotesCreateAssignedToIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_assigned_to_ids_index_error_component import (
            ApiV1NotesCreateAssignedToIdsINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_content_error_component import (
            ApiV1NotesCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_credential_id_error_component import (
            ApiV1NotesCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_criticality_error_component import (
            ApiV1NotesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_debug_mode_error_component import (
            ApiV1NotesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_display_name_error_component import (
            ApiV1NotesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_kind_error_component import (
            ApiV1NotesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_labels_error_component import (
            ApiV1NotesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_name_error_component import (
            ApiV1NotesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_non_field_errors_error_component import (
            ApiV1NotesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_organization_id_error_component import (
            ApiV1NotesCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_parent_note_id_error_component import (
            ApiV1NotesCreateParentNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_platform_service_error_component import (
            ApiV1NotesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_project_id_error_component import (
            ApiV1NotesCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_provider_error_component import (
            ApiV1NotesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_provider_id_error_component import (
            ApiV1NotesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_provider_reference_error_component import (
            ApiV1NotesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_reconciliation_enabled_error_component import (
            ApiV1NotesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_remind_at_error_component import (
            ApiV1NotesCreateRemindAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_resolved_error_component import (
            ApiV1NotesCreateResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_sla_availability_error_component import (
            ApiV1NotesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_sla_target_error_component import (
            ApiV1NotesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_slo_availability_error_component import (
            ApiV1NotesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_slo_target_error_component import (
            ApiV1NotesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_structured_content_error_component import (
            ApiV1NotesCreateStructuredContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_target_availability_error_component import (
            ApiV1NotesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_time_tracked_hours_error_component import (
            ApiV1NotesCreateTimeTrackedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_tolerations_error_component import (
            ApiV1NotesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_tracked_at_error_component import (
            ApiV1NotesCreateTrackedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_vydeo_enabled_error_component import (
            ApiV1NotesCreateVydeoEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_workspace_id_error_component import (
            ApiV1NotesCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateStructuredContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateParentNoteIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateTimeTrackedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateAssignedToIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateAssignedToIdsINDEXErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateRemindAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateTrackedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateVydeoEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesCreateAdditionalRecipientsErrorComponent):
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
        from ..models.api_v1_notes_create_additional_recipients_error_component import (
            ApiV1NotesCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_annotations_error_component import (
            ApiV1NotesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_archived_at_error_component import (
            ApiV1NotesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_archived_error_component import (
            ApiV1NotesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_archived_reason_error_component import (
            ApiV1NotesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_assigned_to_ids_error_component import (
            ApiV1NotesCreateAssignedToIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_assigned_to_ids_index_error_component import (
            ApiV1NotesCreateAssignedToIdsINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_content_error_component import (
            ApiV1NotesCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_credential_id_error_component import (
            ApiV1NotesCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_criticality_error_component import (
            ApiV1NotesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_debug_mode_error_component import (
            ApiV1NotesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_display_name_error_component import (
            ApiV1NotesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_kind_error_component import (
            ApiV1NotesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_labels_error_component import (
            ApiV1NotesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_meeting_duration_minutes_error_component import (
            ApiV1NotesCreateMeetingDurationMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_name_error_component import (
            ApiV1NotesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_non_field_errors_error_component import (
            ApiV1NotesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_organization_id_error_component import (
            ApiV1NotesCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_parent_note_id_error_component import (
            ApiV1NotesCreateParentNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_platform_service_error_component import (
            ApiV1NotesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_project_id_error_component import (
            ApiV1NotesCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_provider_error_component import (
            ApiV1NotesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_provider_id_error_component import (
            ApiV1NotesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_provider_reference_error_component import (
            ApiV1NotesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_reconciliation_enabled_error_component import (
            ApiV1NotesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_remind_at_error_component import (
            ApiV1NotesCreateRemindAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_resolved_error_component import (
            ApiV1NotesCreateResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_sla_availability_error_component import (
            ApiV1NotesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_sla_target_error_component import (
            ApiV1NotesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_slo_availability_error_component import (
            ApiV1NotesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_slo_target_error_component import (
            ApiV1NotesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_structured_content_error_component import (
            ApiV1NotesCreateStructuredContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_target_availability_error_component import (
            ApiV1NotesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_time_tracked_hours_error_component import (
            ApiV1NotesCreateTimeTrackedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_tolerations_error_component import (
            ApiV1NotesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_tracked_at_error_component import (
            ApiV1NotesCreateTrackedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_vydeo_enabled_error_component import (
            ApiV1NotesCreateVydeoEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_create_workspace_id_error_component import (
            ApiV1NotesCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotesCreateAdditionalRecipientsErrorComponent
                | ApiV1NotesCreateAnnotationsErrorComponent
                | ApiV1NotesCreateArchivedAtErrorComponent
                | ApiV1NotesCreateArchivedErrorComponent
                | ApiV1NotesCreateArchivedReasonErrorComponent
                | ApiV1NotesCreateAssignedToIdsErrorComponent
                | ApiV1NotesCreateAssignedToIdsINDEXErrorComponent
                | ApiV1NotesCreateContentErrorComponent
                | ApiV1NotesCreateCredentialIdErrorComponent
                | ApiV1NotesCreateCriticalityErrorComponent
                | ApiV1NotesCreateDebugModeErrorComponent
                | ApiV1NotesCreateDisplayNameErrorComponent
                | ApiV1NotesCreateKindErrorComponent
                | ApiV1NotesCreateLabelsErrorComponent
                | ApiV1NotesCreateMeetingDurationMinutesErrorComponent
                | ApiV1NotesCreateNameErrorComponent
                | ApiV1NotesCreateNonFieldErrorsErrorComponent
                | ApiV1NotesCreateOrganizationIdErrorComponent
                | ApiV1NotesCreateParentNoteIdErrorComponent
                | ApiV1NotesCreatePlatformServiceErrorComponent
                | ApiV1NotesCreateProjectIdErrorComponent
                | ApiV1NotesCreateProviderErrorComponent
                | ApiV1NotesCreateProviderIdErrorComponent
                | ApiV1NotesCreateProviderReferenceErrorComponent
                | ApiV1NotesCreateReconciliationEnabledErrorComponent
                | ApiV1NotesCreateRemindAtErrorComponent
                | ApiV1NotesCreateResolvedErrorComponent
                | ApiV1NotesCreateSlaAvailabilityErrorComponent
                | ApiV1NotesCreateSlaTargetErrorComponent
                | ApiV1NotesCreateSloAvailabilityErrorComponent
                | ApiV1NotesCreateSloTargetErrorComponent
                | ApiV1NotesCreateStructuredContentErrorComponent
                | ApiV1NotesCreateTargetAvailabilityErrorComponent
                | ApiV1NotesCreateTimeTrackedHoursErrorComponent
                | ApiV1NotesCreateTolerationsErrorComponent
                | ApiV1NotesCreateTrackedAtErrorComponent
                | ApiV1NotesCreateVydeoEnabledErrorComponent
                | ApiV1NotesCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_0 = (
                        ApiV1NotesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_1 = ApiV1NotesCreateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_2 = (
                        ApiV1NotesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_3 = ApiV1NotesCreateLabelsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_4 = (
                        ApiV1NotesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_5 = (
                        ApiV1NotesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_6 = (
                        ApiV1NotesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_7 = (
                        ApiV1NotesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_8 = (
                        ApiV1NotesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_9 = (
                        ApiV1NotesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_10 = (
                        ApiV1NotesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_11 = ApiV1NotesCreateKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_notes_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_12 = (
                        ApiV1NotesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_13 = (
                        ApiV1NotesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_14 = (
                        ApiV1NotesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_15 = (
                        ApiV1NotesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_16 = (
                        ApiV1NotesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_17 = (
                        ApiV1NotesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_18 = (
                        ApiV1NotesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_19 = (
                        ApiV1NotesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_20 = (
                        ApiV1NotesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_21 = (
                        ApiV1NotesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_22 = (
                        ApiV1NotesCreateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_23 = (
                        ApiV1NotesCreateStructuredContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_24 = (
                        ApiV1NotesCreateResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_25 = (
                        ApiV1NotesCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_26 = (
                        ApiV1NotesCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_27 = (
                        ApiV1NotesCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_28 = (
                        ApiV1NotesCreateParentNoteIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_29 = (
                        ApiV1NotesCreateTimeTrackedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_30 = (
                        ApiV1NotesCreateAssignedToIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_31 = (
                        ApiV1NotesCreateAssignedToIdsINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_32 = (
                        ApiV1NotesCreateRemindAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_33 = (
                        ApiV1NotesCreateTrackedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_34 = (
                        ApiV1NotesCreateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_35 = (
                        ApiV1NotesCreateVydeoEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_create_error_type_36 = (
                        ApiV1NotesCreateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notes_create_error_type_37 = (
                    ApiV1NotesCreateMeetingDurationMinutesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notes_create_error_type_37

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notes_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notes_create_validation_error.additional_properties = d
        return api_v1_notes_create_validation_error

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
