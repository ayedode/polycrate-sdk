from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_notes_rescan_provider_status_create_additional_recipients_error_component import (
        ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_annotations_error_component import (
        ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_archived_at_error_component import (
        ApiV1NotesRescanProviderStatusCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_archived_error_component import (
        ApiV1NotesRescanProviderStatusCreateArchivedErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_archived_reason_error_component import (
        ApiV1NotesRescanProviderStatusCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_assigned_to_ids_error_component import (
        ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_assigned_to_ids_index_error_component import (
        ApiV1NotesRescanProviderStatusCreateAssignedToIdsINDEXErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_content_error_component import (
        ApiV1NotesRescanProviderStatusCreateContentErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_credential_id_error_component import (
        ApiV1NotesRescanProviderStatusCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_criticality_error_component import (
        ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_debug_mode_error_component import (
        ApiV1NotesRescanProviderStatusCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_display_name_error_component import (
        ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_kind_error_component import (
        ApiV1NotesRescanProviderStatusCreateKindErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_labels_error_component import (
        ApiV1NotesRescanProviderStatusCreateLabelsErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_meeting_duration_minutes_error_component import (
        ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_name_error_component import (
        ApiV1NotesRescanProviderStatusCreateNameErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_non_field_errors_error_component import (
        ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_organization_id_error_component import (
        ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_parent_note_id_error_component import (
        ApiV1NotesRescanProviderStatusCreateParentNoteIdErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_platform_service_error_component import (
        ApiV1NotesRescanProviderStatusCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_project_id_error_component import (
        ApiV1NotesRescanProviderStatusCreateProjectIdErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_provider_error_component import (
        ApiV1NotesRescanProviderStatusCreateProviderErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_provider_id_error_component import (
        ApiV1NotesRescanProviderStatusCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_provider_reference_error_component import (
        ApiV1NotesRescanProviderStatusCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_reconciliation_enabled_error_component import (
        ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_remind_at_error_component import (
        ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_resolved_error_component import (
        ApiV1NotesRescanProviderStatusCreateResolvedErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_sla_availability_error_component import (
        ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_sla_target_error_component import (
        ApiV1NotesRescanProviderStatusCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_slo_availability_error_component import (
        ApiV1NotesRescanProviderStatusCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_slo_target_error_component import (
        ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_structured_content_error_component import (
        ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_target_availability_error_component import (
        ApiV1NotesRescanProviderStatusCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_time_tracked_hours_error_component import (
        ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_tolerations_error_component import (
        ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_tracked_at_error_component import (
        ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_vydeo_enabled_error_component import (
        ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponent,
    )
    from ..models.api_v1_notes_rescan_provider_status_create_workspace_id_error_component import (
        ApiV1NotesRescanProviderStatusCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1NotesRescanProviderStatusCreateValidationError")


@_attrs_define
class ApiV1NotesRescanProviderStatusCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponent |
            ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponent |
            ApiV1NotesRescanProviderStatusCreateArchivedAtErrorComponent |
            ApiV1NotesRescanProviderStatusCreateArchivedErrorComponent |
            ApiV1NotesRescanProviderStatusCreateArchivedReasonErrorComponent |
            ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponent |
            ApiV1NotesRescanProviderStatusCreateAssignedToIdsINDEXErrorComponent |
            ApiV1NotesRescanProviderStatusCreateContentErrorComponent |
            ApiV1NotesRescanProviderStatusCreateCredentialIdErrorComponent |
            ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponent |
            ApiV1NotesRescanProviderStatusCreateDebugModeErrorComponent |
            ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponent |
            ApiV1NotesRescanProviderStatusCreateKindErrorComponent |
            ApiV1NotesRescanProviderStatusCreateLabelsErrorComponent |
            ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponent |
            ApiV1NotesRescanProviderStatusCreateNameErrorComponent |
            ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponent |
            ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponent |
            ApiV1NotesRescanProviderStatusCreateParentNoteIdErrorComponent |
            ApiV1NotesRescanProviderStatusCreatePlatformServiceErrorComponent |
            ApiV1NotesRescanProviderStatusCreateProjectIdErrorComponent |
            ApiV1NotesRescanProviderStatusCreateProviderErrorComponent |
            ApiV1NotesRescanProviderStatusCreateProviderIdErrorComponent |
            ApiV1NotesRescanProviderStatusCreateProviderReferenceErrorComponent |
            ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponent |
            ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponent |
            ApiV1NotesRescanProviderStatusCreateResolvedErrorComponent |
            ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponent |
            ApiV1NotesRescanProviderStatusCreateSlaTargetErrorComponent |
            ApiV1NotesRescanProviderStatusCreateSloAvailabilityErrorComponent |
            ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponent |
            ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponent |
            ApiV1NotesRescanProviderStatusCreateTargetAvailabilityErrorComponent |
            ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponent |
            ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponent |
            ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponent |
            ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponent |
            ApiV1NotesRescanProviderStatusCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponent
        | ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponent
        | ApiV1NotesRescanProviderStatusCreateArchivedAtErrorComponent
        | ApiV1NotesRescanProviderStatusCreateArchivedErrorComponent
        | ApiV1NotesRescanProviderStatusCreateArchivedReasonErrorComponent
        | ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponent
        | ApiV1NotesRescanProviderStatusCreateAssignedToIdsINDEXErrorComponent
        | ApiV1NotesRescanProviderStatusCreateContentErrorComponent
        | ApiV1NotesRescanProviderStatusCreateCredentialIdErrorComponent
        | ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponent
        | ApiV1NotesRescanProviderStatusCreateDebugModeErrorComponent
        | ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponent
        | ApiV1NotesRescanProviderStatusCreateKindErrorComponent
        | ApiV1NotesRescanProviderStatusCreateLabelsErrorComponent
        | ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponent
        | ApiV1NotesRescanProviderStatusCreateNameErrorComponent
        | ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponent
        | ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponent
        | ApiV1NotesRescanProviderStatusCreateParentNoteIdErrorComponent
        | ApiV1NotesRescanProviderStatusCreatePlatformServiceErrorComponent
        | ApiV1NotesRescanProviderStatusCreateProjectIdErrorComponent
        | ApiV1NotesRescanProviderStatusCreateProviderErrorComponent
        | ApiV1NotesRescanProviderStatusCreateProviderIdErrorComponent
        | ApiV1NotesRescanProviderStatusCreateProviderReferenceErrorComponent
        | ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponent
        | ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponent
        | ApiV1NotesRescanProviderStatusCreateResolvedErrorComponent
        | ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponent
        | ApiV1NotesRescanProviderStatusCreateSlaTargetErrorComponent
        | ApiV1NotesRescanProviderStatusCreateSloAvailabilityErrorComponent
        | ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponent
        | ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponent
        | ApiV1NotesRescanProviderStatusCreateTargetAvailabilityErrorComponent
        | ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponent
        | ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponent
        | ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponent
        | ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponent
        | ApiV1NotesRescanProviderStatusCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_notes_rescan_provider_status_create_additional_recipients_error_component import (
            ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_annotations_error_component import (
            ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_archived_at_error_component import (
            ApiV1NotesRescanProviderStatusCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_archived_error_component import (
            ApiV1NotesRescanProviderStatusCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_archived_reason_error_component import (
            ApiV1NotesRescanProviderStatusCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_assigned_to_ids_error_component import (
            ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_assigned_to_ids_index_error_component import (
            ApiV1NotesRescanProviderStatusCreateAssignedToIdsINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_content_error_component import (
            ApiV1NotesRescanProviderStatusCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_credential_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_criticality_error_component import (
            ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_debug_mode_error_component import (
            ApiV1NotesRescanProviderStatusCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_display_name_error_component import (
            ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_kind_error_component import (
            ApiV1NotesRescanProviderStatusCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_labels_error_component import (
            ApiV1NotesRescanProviderStatusCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_name_error_component import (
            ApiV1NotesRescanProviderStatusCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_non_field_errors_error_component import (
            ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_organization_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_parent_note_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateParentNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_platform_service_error_component import (
            ApiV1NotesRescanProviderStatusCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_project_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_provider_error_component import (
            ApiV1NotesRescanProviderStatusCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_provider_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_provider_reference_error_component import (
            ApiV1NotesRescanProviderStatusCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_reconciliation_enabled_error_component import (
            ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_remind_at_error_component import (
            ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_resolved_error_component import (
            ApiV1NotesRescanProviderStatusCreateResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_sla_availability_error_component import (
            ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_sla_target_error_component import (
            ApiV1NotesRescanProviderStatusCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_slo_availability_error_component import (
            ApiV1NotesRescanProviderStatusCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_slo_target_error_component import (
            ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_structured_content_error_component import (
            ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_target_availability_error_component import (
            ApiV1NotesRescanProviderStatusCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_time_tracked_hours_error_component import (
            ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_tolerations_error_component import (
            ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_tracked_at_error_component import (
            ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_vydeo_enabled_error_component import (
            ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_workspace_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateParentNoteIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateAssignedToIdsINDEXErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponent):
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
        from ..models.api_v1_notes_rescan_provider_status_create_additional_recipients_error_component import (
            ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_annotations_error_component import (
            ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_archived_at_error_component import (
            ApiV1NotesRescanProviderStatusCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_archived_error_component import (
            ApiV1NotesRescanProviderStatusCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_archived_reason_error_component import (
            ApiV1NotesRescanProviderStatusCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_assigned_to_ids_error_component import (
            ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_assigned_to_ids_index_error_component import (
            ApiV1NotesRescanProviderStatusCreateAssignedToIdsINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_content_error_component import (
            ApiV1NotesRescanProviderStatusCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_credential_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_criticality_error_component import (
            ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_debug_mode_error_component import (
            ApiV1NotesRescanProviderStatusCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_display_name_error_component import (
            ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_kind_error_component import (
            ApiV1NotesRescanProviderStatusCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_labels_error_component import (
            ApiV1NotesRescanProviderStatusCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_meeting_duration_minutes_error_component import (
            ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_name_error_component import (
            ApiV1NotesRescanProviderStatusCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_non_field_errors_error_component import (
            ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_organization_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_parent_note_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateParentNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_platform_service_error_component import (
            ApiV1NotesRescanProviderStatusCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_project_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_provider_error_component import (
            ApiV1NotesRescanProviderStatusCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_provider_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_provider_reference_error_component import (
            ApiV1NotesRescanProviderStatusCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_reconciliation_enabled_error_component import (
            ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_remind_at_error_component import (
            ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_resolved_error_component import (
            ApiV1NotesRescanProviderStatusCreateResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_sla_availability_error_component import (
            ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_sla_target_error_component import (
            ApiV1NotesRescanProviderStatusCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_slo_availability_error_component import (
            ApiV1NotesRescanProviderStatusCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_slo_target_error_component import (
            ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_structured_content_error_component import (
            ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_target_availability_error_component import (
            ApiV1NotesRescanProviderStatusCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_time_tracked_hours_error_component import (
            ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_tolerations_error_component import (
            ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_tracked_at_error_component import (
            ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_vydeo_enabled_error_component import (
            ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_notes_rescan_provider_status_create_workspace_id_error_component import (
            ApiV1NotesRescanProviderStatusCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponent
                | ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponent
                | ApiV1NotesRescanProviderStatusCreateArchivedAtErrorComponent
                | ApiV1NotesRescanProviderStatusCreateArchivedErrorComponent
                | ApiV1NotesRescanProviderStatusCreateArchivedReasonErrorComponent
                | ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponent
                | ApiV1NotesRescanProviderStatusCreateAssignedToIdsINDEXErrorComponent
                | ApiV1NotesRescanProviderStatusCreateContentErrorComponent
                | ApiV1NotesRescanProviderStatusCreateCredentialIdErrorComponent
                | ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponent
                | ApiV1NotesRescanProviderStatusCreateDebugModeErrorComponent
                | ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponent
                | ApiV1NotesRescanProviderStatusCreateKindErrorComponent
                | ApiV1NotesRescanProviderStatusCreateLabelsErrorComponent
                | ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponent
                | ApiV1NotesRescanProviderStatusCreateNameErrorComponent
                | ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponent
                | ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponent
                | ApiV1NotesRescanProviderStatusCreateParentNoteIdErrorComponent
                | ApiV1NotesRescanProviderStatusCreatePlatformServiceErrorComponent
                | ApiV1NotesRescanProviderStatusCreateProjectIdErrorComponent
                | ApiV1NotesRescanProviderStatusCreateProviderErrorComponent
                | ApiV1NotesRescanProviderStatusCreateProviderIdErrorComponent
                | ApiV1NotesRescanProviderStatusCreateProviderReferenceErrorComponent
                | ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponent
                | ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponent
                | ApiV1NotesRescanProviderStatusCreateResolvedErrorComponent
                | ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponent
                | ApiV1NotesRescanProviderStatusCreateSlaTargetErrorComponent
                | ApiV1NotesRescanProviderStatusCreateSloAvailabilityErrorComponent
                | ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponent
                | ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponent
                | ApiV1NotesRescanProviderStatusCreateTargetAvailabilityErrorComponent
                | ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponent
                | ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponent
                | ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponent
                | ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponent
                | ApiV1NotesRescanProviderStatusCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_0 = (
                        ApiV1NotesRescanProviderStatusCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_1 = (
                        ApiV1NotesRescanProviderStatusCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_2 = (
                        ApiV1NotesRescanProviderStatusCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_3 = (
                        ApiV1NotesRescanProviderStatusCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_4 = (
                        ApiV1NotesRescanProviderStatusCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_5 = (
                        ApiV1NotesRescanProviderStatusCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_6 = (
                        ApiV1NotesRescanProviderStatusCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_7 = (
                        ApiV1NotesRescanProviderStatusCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_8 = (
                        ApiV1NotesRescanProviderStatusCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_9 = (
                        ApiV1NotesRescanProviderStatusCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_10 = (
                        ApiV1NotesRescanProviderStatusCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_11 = (
                        ApiV1NotesRescanProviderStatusCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_12 = (
                        ApiV1NotesRescanProviderStatusCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_13 = (
                        ApiV1NotesRescanProviderStatusCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_14 = (
                        ApiV1NotesRescanProviderStatusCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_15 = (
                        ApiV1NotesRescanProviderStatusCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_16 = (
                        ApiV1NotesRescanProviderStatusCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_17 = (
                        ApiV1NotesRescanProviderStatusCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_18 = (
                        ApiV1NotesRescanProviderStatusCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_19 = (
                        ApiV1NotesRescanProviderStatusCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_20 = (
                        ApiV1NotesRescanProviderStatusCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_21 = (
                        ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_22 = (
                        ApiV1NotesRescanProviderStatusCreateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_23 = (
                        ApiV1NotesRescanProviderStatusCreateStructuredContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_24 = (
                        ApiV1NotesRescanProviderStatusCreateResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_25 = (
                        ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_26 = (
                        ApiV1NotesRescanProviderStatusCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_27 = (
                        ApiV1NotesRescanProviderStatusCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_28 = (
                        ApiV1NotesRescanProviderStatusCreateParentNoteIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_29 = (
                        ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_30 = (
                        ApiV1NotesRescanProviderStatusCreateAssignedToIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_31 = (
                        ApiV1NotesRescanProviderStatusCreateAssignedToIdsINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_32 = (
                        ApiV1NotesRescanProviderStatusCreateRemindAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_33 = (
                        ApiV1NotesRescanProviderStatusCreateTrackedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_34 = (
                        ApiV1NotesRescanProviderStatusCreateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_35 = (
                        ApiV1NotesRescanProviderStatusCreateVydeoEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_36 = (
                        ApiV1NotesRescanProviderStatusCreateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_37 = (
                    ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_notes_rescan_provider_status_create_error_type_37

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_notes_rescan_provider_status_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_notes_rescan_provider_status_create_validation_error.additional_properties = d
        return api_v1_notes_rescan_provider_status_create_validation_error

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
