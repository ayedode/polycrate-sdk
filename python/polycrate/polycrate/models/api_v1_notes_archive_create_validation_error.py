from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notes_archive_create_additional_recipients_error_component import (
        ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_annotations_error_component import (
        ApiV1NotesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_archived_at_error_component import (
        ApiV1NotesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_archived_error_component import (
        ApiV1NotesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_archived_reason_error_component import (
        ApiV1NotesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_assigned_to_ids_error_component import (
        ApiV1NotesArchiveCreateAssignedToIdsErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_assigned_to_ids_index_error_component import (
        ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_content_error_component import (
        ApiV1NotesArchiveCreateContentErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_credential_id_error_component import (
        ApiV1NotesArchiveCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_criticality_error_component import (
        ApiV1NotesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_debug_mode_error_component import (
        ApiV1NotesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_display_name_error_component import (
        ApiV1NotesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_kind_error_component import ApiV1NotesArchiveCreateKindErrorComponent
    from ..models.api_v1_notes_archive_create_labels_error_component import ApiV1NotesArchiveCreateLabelsErrorComponent
    from ..models.api_v1_notes_archive_create_meeting_duration_minutes_error_component import (
        ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_name_error_component import ApiV1NotesArchiveCreateNameErrorComponent
    from ..models.api_v1_notes_archive_create_non_field_errors_error_component import (
        ApiV1NotesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_organization_id_error_component import (
        ApiV1NotesArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_parent_note_id_error_component import (
        ApiV1NotesArchiveCreateParentNoteIdErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_platform_service_error_component import (
        ApiV1NotesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_project_id_error_component import (
        ApiV1NotesArchiveCreateProjectIdErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_provider_error_component import (
        ApiV1NotesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_provider_id_error_component import (
        ApiV1NotesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_provider_reference_error_component import (
        ApiV1NotesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_reconciliation_enabled_error_component import (
        ApiV1NotesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_remind_at_error_component import (
        ApiV1NotesArchiveCreateRemindAtErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_resolved_error_component import (
        ApiV1NotesArchiveCreateResolvedErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_sla_availability_error_component import (
        ApiV1NotesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_sla_target_error_component import (
        ApiV1NotesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_slo_availability_error_component import (
        ApiV1NotesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_slo_target_error_component import (
        ApiV1NotesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_structured_content_error_component import (
        ApiV1NotesArchiveCreateStructuredContentErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_target_availability_error_component import (
        ApiV1NotesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_time_tracked_hours_error_component import (
        ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_tolerations_error_component import (
        ApiV1NotesArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_tracked_at_error_component import (
        ApiV1NotesArchiveCreateTrackedAtErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_vydeo_enabled_error_component import (
        ApiV1NotesArchiveCreateVydeoEnabledErrorComponent,
    )
    from ..models.api_v1_notes_archive_create_workspace_id_error_component import (
        ApiV1NotesArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotesArchiveCreateValidationError")


@_attrs_define
class ApiV1NotesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponent |
            ApiV1NotesArchiveCreateAnnotationsErrorComponent | ApiV1NotesArchiveCreateArchivedAtErrorComponent |
            ApiV1NotesArchiveCreateArchivedErrorComponent | ApiV1NotesArchiveCreateArchivedReasonErrorComponent |
            ApiV1NotesArchiveCreateAssignedToIdsErrorComponent | ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponent |
            ApiV1NotesArchiveCreateContentErrorComponent | ApiV1NotesArchiveCreateCredentialIdErrorComponent |
            ApiV1NotesArchiveCreateCriticalityErrorComponent | ApiV1NotesArchiveCreateDebugModeErrorComponent |
            ApiV1NotesArchiveCreateDisplayNameErrorComponent | ApiV1NotesArchiveCreateKindErrorComponent |
            ApiV1NotesArchiveCreateLabelsErrorComponent | ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponent |
            ApiV1NotesArchiveCreateNameErrorComponent | ApiV1NotesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1NotesArchiveCreateOrganizationIdErrorComponent | ApiV1NotesArchiveCreateParentNoteIdErrorComponent |
            ApiV1NotesArchiveCreatePlatformServiceErrorComponent | ApiV1NotesArchiveCreateProjectIdErrorComponent |
            ApiV1NotesArchiveCreateProviderErrorComponent | ApiV1NotesArchiveCreateProviderIdErrorComponent |
            ApiV1NotesArchiveCreateProviderReferenceErrorComponent |
            ApiV1NotesArchiveCreateReconciliationEnabledErrorComponent | ApiV1NotesArchiveCreateRemindAtErrorComponent |
            ApiV1NotesArchiveCreateResolvedErrorComponent | ApiV1NotesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1NotesArchiveCreateSlaTargetErrorComponent | ApiV1NotesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1NotesArchiveCreateSloTargetErrorComponent | ApiV1NotesArchiveCreateStructuredContentErrorComponent |
            ApiV1NotesArchiveCreateTargetAvailabilityErrorComponent | ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponent
            | ApiV1NotesArchiveCreateTolerationsErrorComponent | ApiV1NotesArchiveCreateTrackedAtErrorComponent |
            ApiV1NotesArchiveCreateVydeoEnabledErrorComponent | ApiV1NotesArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponent
        | ApiV1NotesArchiveCreateAnnotationsErrorComponent
        | ApiV1NotesArchiveCreateArchivedAtErrorComponent
        | ApiV1NotesArchiveCreateArchivedErrorComponent
        | ApiV1NotesArchiveCreateArchivedReasonErrorComponent
        | ApiV1NotesArchiveCreateAssignedToIdsErrorComponent
        | ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponent
        | ApiV1NotesArchiveCreateContentErrorComponent
        | ApiV1NotesArchiveCreateCredentialIdErrorComponent
        | ApiV1NotesArchiveCreateCriticalityErrorComponent
        | ApiV1NotesArchiveCreateDebugModeErrorComponent
        | ApiV1NotesArchiveCreateDisplayNameErrorComponent
        | ApiV1NotesArchiveCreateKindErrorComponent
        | ApiV1NotesArchiveCreateLabelsErrorComponent
        | ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponent
        | ApiV1NotesArchiveCreateNameErrorComponent
        | ApiV1NotesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1NotesArchiveCreateOrganizationIdErrorComponent
        | ApiV1NotesArchiveCreateParentNoteIdErrorComponent
        | ApiV1NotesArchiveCreatePlatformServiceErrorComponent
        | ApiV1NotesArchiveCreateProjectIdErrorComponent
        | ApiV1NotesArchiveCreateProviderErrorComponent
        | ApiV1NotesArchiveCreateProviderIdErrorComponent
        | ApiV1NotesArchiveCreateProviderReferenceErrorComponent
        | ApiV1NotesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1NotesArchiveCreateRemindAtErrorComponent
        | ApiV1NotesArchiveCreateResolvedErrorComponent
        | ApiV1NotesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1NotesArchiveCreateSlaTargetErrorComponent
        | ApiV1NotesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1NotesArchiveCreateSloTargetErrorComponent
        | ApiV1NotesArchiveCreateStructuredContentErrorComponent
        | ApiV1NotesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponent
        | ApiV1NotesArchiveCreateTolerationsErrorComponent
        | ApiV1NotesArchiveCreateTrackedAtErrorComponent
        | ApiV1NotesArchiveCreateVydeoEnabledErrorComponent
        | ApiV1NotesArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notes_archive_create_additional_recipients_error_component import (
            ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_annotations_error_component import (
            ApiV1NotesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_archived_at_error_component import (
            ApiV1NotesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_archived_error_component import (
            ApiV1NotesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_archived_reason_error_component import (
            ApiV1NotesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_assigned_to_ids_error_component import (
            ApiV1NotesArchiveCreateAssignedToIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_assigned_to_ids_index_error_component import (
            ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_content_error_component import (
            ApiV1NotesArchiveCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_credential_id_error_component import (
            ApiV1NotesArchiveCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_criticality_error_component import (
            ApiV1NotesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_debug_mode_error_component import (
            ApiV1NotesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_display_name_error_component import (
            ApiV1NotesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_kind_error_component import (
            ApiV1NotesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_labels_error_component import (
            ApiV1NotesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_name_error_component import (
            ApiV1NotesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_non_field_errors_error_component import (
            ApiV1NotesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_organization_id_error_component import (
            ApiV1NotesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_parent_note_id_error_component import (
            ApiV1NotesArchiveCreateParentNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_platform_service_error_component import (
            ApiV1NotesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_project_id_error_component import (
            ApiV1NotesArchiveCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_provider_error_component import (
            ApiV1NotesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_provider_id_error_component import (
            ApiV1NotesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_provider_reference_error_component import (
            ApiV1NotesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_reconciliation_enabled_error_component import (
            ApiV1NotesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_remind_at_error_component import (
            ApiV1NotesArchiveCreateRemindAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_resolved_error_component import (
            ApiV1NotesArchiveCreateResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_sla_availability_error_component import (
            ApiV1NotesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_sla_target_error_component import (
            ApiV1NotesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_slo_availability_error_component import (
            ApiV1NotesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_slo_target_error_component import (
            ApiV1NotesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_structured_content_error_component import (
            ApiV1NotesArchiveCreateStructuredContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_target_availability_error_component import (
            ApiV1NotesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_time_tracked_hours_error_component import (
            ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_tolerations_error_component import (
            ApiV1NotesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_tracked_at_error_component import (
            ApiV1NotesArchiveCreateTrackedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_vydeo_enabled_error_component import (
            ApiV1NotesArchiveCreateVydeoEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_workspace_id_error_component import (
            ApiV1NotesArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateStructuredContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateParentNoteIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateAssignedToIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateRemindAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateTrackedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateVydeoEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponent):
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
        from ..models.api_v1_notes_archive_create_additional_recipients_error_component import (
            ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_annotations_error_component import (
            ApiV1NotesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_archived_at_error_component import (
            ApiV1NotesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_archived_error_component import (
            ApiV1NotesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_archived_reason_error_component import (
            ApiV1NotesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_assigned_to_ids_error_component import (
            ApiV1NotesArchiveCreateAssignedToIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_assigned_to_ids_index_error_component import (
            ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_content_error_component import (
            ApiV1NotesArchiveCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_credential_id_error_component import (
            ApiV1NotesArchiveCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_criticality_error_component import (
            ApiV1NotesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_debug_mode_error_component import (
            ApiV1NotesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_display_name_error_component import (
            ApiV1NotesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_kind_error_component import (
            ApiV1NotesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_labels_error_component import (
            ApiV1NotesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_meeting_duration_minutes_error_component import (
            ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_name_error_component import (
            ApiV1NotesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_non_field_errors_error_component import (
            ApiV1NotesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_organization_id_error_component import (
            ApiV1NotesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_parent_note_id_error_component import (
            ApiV1NotesArchiveCreateParentNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_platform_service_error_component import (
            ApiV1NotesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_project_id_error_component import (
            ApiV1NotesArchiveCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_provider_error_component import (
            ApiV1NotesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_provider_id_error_component import (
            ApiV1NotesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_provider_reference_error_component import (
            ApiV1NotesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_reconciliation_enabled_error_component import (
            ApiV1NotesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_remind_at_error_component import (
            ApiV1NotesArchiveCreateRemindAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_resolved_error_component import (
            ApiV1NotesArchiveCreateResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_sla_availability_error_component import (
            ApiV1NotesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_sla_target_error_component import (
            ApiV1NotesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_slo_availability_error_component import (
            ApiV1NotesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_slo_target_error_component import (
            ApiV1NotesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_structured_content_error_component import (
            ApiV1NotesArchiveCreateStructuredContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_target_availability_error_component import (
            ApiV1NotesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_time_tracked_hours_error_component import (
            ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_tolerations_error_component import (
            ApiV1NotesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_tracked_at_error_component import (
            ApiV1NotesArchiveCreateTrackedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_vydeo_enabled_error_component import (
            ApiV1NotesArchiveCreateVydeoEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_archive_create_workspace_id_error_component import (
            ApiV1NotesArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponent
                | ApiV1NotesArchiveCreateAnnotationsErrorComponent
                | ApiV1NotesArchiveCreateArchivedAtErrorComponent
                | ApiV1NotesArchiveCreateArchivedErrorComponent
                | ApiV1NotesArchiveCreateArchivedReasonErrorComponent
                | ApiV1NotesArchiveCreateAssignedToIdsErrorComponent
                | ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponent
                | ApiV1NotesArchiveCreateContentErrorComponent
                | ApiV1NotesArchiveCreateCredentialIdErrorComponent
                | ApiV1NotesArchiveCreateCriticalityErrorComponent
                | ApiV1NotesArchiveCreateDebugModeErrorComponent
                | ApiV1NotesArchiveCreateDisplayNameErrorComponent
                | ApiV1NotesArchiveCreateKindErrorComponent
                | ApiV1NotesArchiveCreateLabelsErrorComponent
                | ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponent
                | ApiV1NotesArchiveCreateNameErrorComponent
                | ApiV1NotesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1NotesArchiveCreateOrganizationIdErrorComponent
                | ApiV1NotesArchiveCreateParentNoteIdErrorComponent
                | ApiV1NotesArchiveCreatePlatformServiceErrorComponent
                | ApiV1NotesArchiveCreateProjectIdErrorComponent
                | ApiV1NotesArchiveCreateProviderErrorComponent
                | ApiV1NotesArchiveCreateProviderIdErrorComponent
                | ApiV1NotesArchiveCreateProviderReferenceErrorComponent
                | ApiV1NotesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1NotesArchiveCreateRemindAtErrorComponent
                | ApiV1NotesArchiveCreateResolvedErrorComponent
                | ApiV1NotesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1NotesArchiveCreateSlaTargetErrorComponent
                | ApiV1NotesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1NotesArchiveCreateSloTargetErrorComponent
                | ApiV1NotesArchiveCreateStructuredContentErrorComponent
                | ApiV1NotesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponent
                | ApiV1NotesArchiveCreateTolerationsErrorComponent
                | ApiV1NotesArchiveCreateTrackedAtErrorComponent
                | ApiV1NotesArchiveCreateVydeoEnabledErrorComponent
                | ApiV1NotesArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_0 = (
                        ApiV1NotesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_1 = (
                        ApiV1NotesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_2 = (
                        ApiV1NotesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_3 = (
                        ApiV1NotesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_4 = (
                        ApiV1NotesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_5 = (
                        ApiV1NotesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_6 = (
                        ApiV1NotesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_7 = (
                        ApiV1NotesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_8 = (
                        ApiV1NotesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_9 = (
                        ApiV1NotesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_10 = (
                        ApiV1NotesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_11 = (
                        ApiV1NotesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_12 = (
                        ApiV1NotesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_13 = (
                        ApiV1NotesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_14 = (
                        ApiV1NotesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_15 = (
                        ApiV1NotesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_16 = (
                        ApiV1NotesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_17 = (
                        ApiV1NotesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_18 = (
                        ApiV1NotesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_19 = (
                        ApiV1NotesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_20 = (
                        ApiV1NotesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_21 = (
                        ApiV1NotesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_22 = (
                        ApiV1NotesArchiveCreateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_23 = (
                        ApiV1NotesArchiveCreateStructuredContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_24 = (
                        ApiV1NotesArchiveCreateResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_25 = (
                        ApiV1NotesArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_26 = (
                        ApiV1NotesArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_27 = (
                        ApiV1NotesArchiveCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_28 = (
                        ApiV1NotesArchiveCreateParentNoteIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_29 = (
                        ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_30 = (
                        ApiV1NotesArchiveCreateAssignedToIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_31 = (
                        ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_32 = (
                        ApiV1NotesArchiveCreateRemindAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_33 = (
                        ApiV1NotesArchiveCreateTrackedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_34 = (
                        ApiV1NotesArchiveCreateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_35 = (
                        ApiV1NotesArchiveCreateVydeoEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_archive_create_error_type_36 = (
                        ApiV1NotesArchiveCreateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notes_archive_create_error_type_37 = (
                    ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notes_archive_create_error_type_37

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notes_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notes_archive_create_validation_error.additional_properties = d
        return api_v1_notes_archive_create_validation_error

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
