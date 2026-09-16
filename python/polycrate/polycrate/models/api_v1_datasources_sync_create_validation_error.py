from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_datasources_sync_create_annotations_error_component import (
        ApiV1DatasourcesSyncCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_archived_at_error_component import (
        ApiV1DatasourcesSyncCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_archived_error_component import (
        ApiV1DatasourcesSyncCreateArchivedErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_archived_reason_error_component import (
        ApiV1DatasourcesSyncCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_create_incidents_error_component import (
        ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_create_incidents_without_resources_error_component import (
        ApiV1DatasourcesSyncCreateCreateIncidentsWithoutResourcesErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_create_maintenance_as_draft_error_component import (
        ApiV1DatasourcesSyncCreateCreateMaintenanceAsDraftErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_create_notes_resolved_error_component import (
        ApiV1DatasourcesSyncCreateCreateNotesResolvedErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_criticality_error_component import (
        ApiV1DatasourcesSyncCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_datasource_url_error_component import (
        ApiV1DatasourcesSyncCreateDatasourceUrlErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_debug_mode_error_component import (
        ApiV1DatasourcesSyncCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_display_name_error_component import (
        ApiV1DatasourcesSyncCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_is_enabled_error_component import (
        ApiV1DatasourcesSyncCreateIsEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_kind_error_component import (
        ApiV1DatasourcesSyncCreateKindErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_labels_error_component import (
        ApiV1DatasourcesSyncCreateLabelsErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_last_sync_error_component import (
        ApiV1DatasourcesSyncCreateLastSyncErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_last_sync_error_error_component import (
        ApiV1DatasourcesSyncCreateLastSyncErrorErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_name_error_component import (
        ApiV1DatasourcesSyncCreateNameErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_non_field_errors_error_component import (
        ApiV1DatasourcesSyncCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_note_kind_error_component import (
        ApiV1DatasourcesSyncCreateNoteKindErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_note_organization_id_error_component import (
        ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_note_workspace_id_error_component import (
        ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_platform_service_error_component import (
        ApiV1DatasourcesSyncCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_provider_entity_id_error_component import (
        ApiV1DatasourcesSyncCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_provider_error_component import (
        ApiV1DatasourcesSyncCreateProviderErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_provider_id_error_component import (
        ApiV1DatasourcesSyncCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_provider_reference_error_component import (
        ApiV1DatasourcesSyncCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_reconciliation_enabled_error_component import (
        ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_sla_availability_error_component import (
        ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_sla_target_error_component import (
        ApiV1DatasourcesSyncCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_slo_availability_error_component import (
        ApiV1DatasourcesSyncCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_slo_target_error_component import (
        ApiV1DatasourcesSyncCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_sync_interval_minutes_error_component import (
        ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_target_availability_error_component import (
        ApiV1DatasourcesSyncCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_sync_create_tolerations_error_component import (
        ApiV1DatasourcesSyncCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DatasourcesSyncCreateValidationError")


@_attrs_define
class ApiV1DatasourcesSyncCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DatasourcesSyncCreateAnnotationsErrorComponent |
            ApiV1DatasourcesSyncCreateArchivedAtErrorComponent | ApiV1DatasourcesSyncCreateArchivedErrorComponent |
            ApiV1DatasourcesSyncCreateArchivedReasonErrorComponent | ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponent
            | ApiV1DatasourcesSyncCreateCreateIncidentsWithoutResourcesErrorComponent |
            ApiV1DatasourcesSyncCreateCreateMaintenanceAsDraftErrorComponent |
            ApiV1DatasourcesSyncCreateCreateNotesResolvedErrorComponent |
            ApiV1DatasourcesSyncCreateCriticalityErrorComponent | ApiV1DatasourcesSyncCreateDatasourceUrlErrorComponent |
            ApiV1DatasourcesSyncCreateDebugModeErrorComponent | ApiV1DatasourcesSyncCreateDisplayNameErrorComponent |
            ApiV1DatasourcesSyncCreateIsEnabledErrorComponent | ApiV1DatasourcesSyncCreateKindErrorComponent |
            ApiV1DatasourcesSyncCreateLabelsErrorComponent | ApiV1DatasourcesSyncCreateLastSyncErrorComponent |
            ApiV1DatasourcesSyncCreateLastSyncErrorErrorComponent | ApiV1DatasourcesSyncCreateNameErrorComponent |
            ApiV1DatasourcesSyncCreateNonFieldErrorsErrorComponent | ApiV1DatasourcesSyncCreateNoteKindErrorComponent |
            ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponent |
            ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponent |
            ApiV1DatasourcesSyncCreatePlatformServiceErrorComponent |
            ApiV1DatasourcesSyncCreateProviderEntityIdErrorComponent | ApiV1DatasourcesSyncCreateProviderErrorComponent |
            ApiV1DatasourcesSyncCreateProviderIdErrorComponent | ApiV1DatasourcesSyncCreateProviderReferenceErrorComponent |
            ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponent |
            ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponent | ApiV1DatasourcesSyncCreateSlaTargetErrorComponent |
            ApiV1DatasourcesSyncCreateSloAvailabilityErrorComponent | ApiV1DatasourcesSyncCreateSloTargetErrorComponent |
            ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponent |
            ApiV1DatasourcesSyncCreateTargetAvailabilityErrorComponent |
            ApiV1DatasourcesSyncCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DatasourcesSyncCreateAnnotationsErrorComponent
        | ApiV1DatasourcesSyncCreateArchivedAtErrorComponent
        | ApiV1DatasourcesSyncCreateArchivedErrorComponent
        | ApiV1DatasourcesSyncCreateArchivedReasonErrorComponent
        | ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponent
        | ApiV1DatasourcesSyncCreateCreateIncidentsWithoutResourcesErrorComponent
        | ApiV1DatasourcesSyncCreateCreateMaintenanceAsDraftErrorComponent
        | ApiV1DatasourcesSyncCreateCreateNotesResolvedErrorComponent
        | ApiV1DatasourcesSyncCreateCriticalityErrorComponent
        | ApiV1DatasourcesSyncCreateDatasourceUrlErrorComponent
        | ApiV1DatasourcesSyncCreateDebugModeErrorComponent
        | ApiV1DatasourcesSyncCreateDisplayNameErrorComponent
        | ApiV1DatasourcesSyncCreateIsEnabledErrorComponent
        | ApiV1DatasourcesSyncCreateKindErrorComponent
        | ApiV1DatasourcesSyncCreateLabelsErrorComponent
        | ApiV1DatasourcesSyncCreateLastSyncErrorComponent
        | ApiV1DatasourcesSyncCreateLastSyncErrorErrorComponent
        | ApiV1DatasourcesSyncCreateNameErrorComponent
        | ApiV1DatasourcesSyncCreateNonFieldErrorsErrorComponent
        | ApiV1DatasourcesSyncCreateNoteKindErrorComponent
        | ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponent
        | ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponent
        | ApiV1DatasourcesSyncCreatePlatformServiceErrorComponent
        | ApiV1DatasourcesSyncCreateProviderEntityIdErrorComponent
        | ApiV1DatasourcesSyncCreateProviderErrorComponent
        | ApiV1DatasourcesSyncCreateProviderIdErrorComponent
        | ApiV1DatasourcesSyncCreateProviderReferenceErrorComponent
        | ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponent
        | ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponent
        | ApiV1DatasourcesSyncCreateSlaTargetErrorComponent
        | ApiV1DatasourcesSyncCreateSloAvailabilityErrorComponent
        | ApiV1DatasourcesSyncCreateSloTargetErrorComponent
        | ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponent
        | ApiV1DatasourcesSyncCreateTargetAvailabilityErrorComponent
        | ApiV1DatasourcesSyncCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_datasources_sync_create_annotations_error_component import (
            ApiV1DatasourcesSyncCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_archived_at_error_component import (
            ApiV1DatasourcesSyncCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_archived_error_component import (
            ApiV1DatasourcesSyncCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_archived_reason_error_component import (
            ApiV1DatasourcesSyncCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_create_incidents_error_component import (
            ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesSyncCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesSyncCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesSyncCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_criticality_error_component import (
            ApiV1DatasourcesSyncCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_datasource_url_error_component import (
            ApiV1DatasourcesSyncCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_debug_mode_error_component import (
            ApiV1DatasourcesSyncCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_display_name_error_component import (
            ApiV1DatasourcesSyncCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_is_enabled_error_component import (
            ApiV1DatasourcesSyncCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_kind_error_component import (
            ApiV1DatasourcesSyncCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_labels_error_component import (
            ApiV1DatasourcesSyncCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_last_sync_error_component import (
            ApiV1DatasourcesSyncCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_last_sync_error_error_component import (
            ApiV1DatasourcesSyncCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_name_error_component import (
            ApiV1DatasourcesSyncCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_non_field_errors_error_component import (
            ApiV1DatasourcesSyncCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_note_kind_error_component import (
            ApiV1DatasourcesSyncCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_note_organization_id_error_component import (
            ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_note_workspace_id_error_component import (
            ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_platform_service_error_component import (
            ApiV1DatasourcesSyncCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_provider_error_component import (
            ApiV1DatasourcesSyncCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_provider_id_error_component import (
            ApiV1DatasourcesSyncCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_provider_reference_error_component import (
            ApiV1DatasourcesSyncCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_sla_availability_error_component import (
            ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_sla_target_error_component import (
            ApiV1DatasourcesSyncCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_slo_availability_error_component import (
            ApiV1DatasourcesSyncCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_slo_target_error_component import (
            ApiV1DatasourcesSyncCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_target_availability_error_component import (
            ApiV1DatasourcesSyncCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_tolerations_error_component import (
            ApiV1DatasourcesSyncCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DatasourcesSyncCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateDatasourceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateNoteKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateCreateNotesResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateCreateMaintenanceAsDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateCreateIncidentsWithoutResourcesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateLastSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesSyncCreateLastSyncErrorErrorComponent):
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
        from ..models.api_v1_datasources_sync_create_annotations_error_component import (
            ApiV1DatasourcesSyncCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_archived_at_error_component import (
            ApiV1DatasourcesSyncCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_archived_error_component import (
            ApiV1DatasourcesSyncCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_archived_reason_error_component import (
            ApiV1DatasourcesSyncCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_create_incidents_error_component import (
            ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesSyncCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesSyncCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesSyncCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_criticality_error_component import (
            ApiV1DatasourcesSyncCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_datasource_url_error_component import (
            ApiV1DatasourcesSyncCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_debug_mode_error_component import (
            ApiV1DatasourcesSyncCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_display_name_error_component import (
            ApiV1DatasourcesSyncCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_is_enabled_error_component import (
            ApiV1DatasourcesSyncCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_kind_error_component import (
            ApiV1DatasourcesSyncCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_labels_error_component import (
            ApiV1DatasourcesSyncCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_last_sync_error_component import (
            ApiV1DatasourcesSyncCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_last_sync_error_error_component import (
            ApiV1DatasourcesSyncCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_name_error_component import (
            ApiV1DatasourcesSyncCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_non_field_errors_error_component import (
            ApiV1DatasourcesSyncCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_note_kind_error_component import (
            ApiV1DatasourcesSyncCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_note_organization_id_error_component import (
            ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_note_workspace_id_error_component import (
            ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_platform_service_error_component import (
            ApiV1DatasourcesSyncCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_provider_entity_id_error_component import (
            ApiV1DatasourcesSyncCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_provider_error_component import (
            ApiV1DatasourcesSyncCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_provider_id_error_component import (
            ApiV1DatasourcesSyncCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_provider_reference_error_component import (
            ApiV1DatasourcesSyncCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_sla_availability_error_component import (
            ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_sla_target_error_component import (
            ApiV1DatasourcesSyncCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_slo_availability_error_component import (
            ApiV1DatasourcesSyncCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_slo_target_error_component import (
            ApiV1DatasourcesSyncCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_target_availability_error_component import (
            ApiV1DatasourcesSyncCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_sync_create_tolerations_error_component import (
            ApiV1DatasourcesSyncCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DatasourcesSyncCreateAnnotationsErrorComponent
                | ApiV1DatasourcesSyncCreateArchivedAtErrorComponent
                | ApiV1DatasourcesSyncCreateArchivedErrorComponent
                | ApiV1DatasourcesSyncCreateArchivedReasonErrorComponent
                | ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponent
                | ApiV1DatasourcesSyncCreateCreateIncidentsWithoutResourcesErrorComponent
                | ApiV1DatasourcesSyncCreateCreateMaintenanceAsDraftErrorComponent
                | ApiV1DatasourcesSyncCreateCreateNotesResolvedErrorComponent
                | ApiV1DatasourcesSyncCreateCriticalityErrorComponent
                | ApiV1DatasourcesSyncCreateDatasourceUrlErrorComponent
                | ApiV1DatasourcesSyncCreateDebugModeErrorComponent
                | ApiV1DatasourcesSyncCreateDisplayNameErrorComponent
                | ApiV1DatasourcesSyncCreateIsEnabledErrorComponent
                | ApiV1DatasourcesSyncCreateKindErrorComponent
                | ApiV1DatasourcesSyncCreateLabelsErrorComponent
                | ApiV1DatasourcesSyncCreateLastSyncErrorComponent
                | ApiV1DatasourcesSyncCreateLastSyncErrorErrorComponent
                | ApiV1DatasourcesSyncCreateNameErrorComponent
                | ApiV1DatasourcesSyncCreateNonFieldErrorsErrorComponent
                | ApiV1DatasourcesSyncCreateNoteKindErrorComponent
                | ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponent
                | ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponent
                | ApiV1DatasourcesSyncCreatePlatformServiceErrorComponent
                | ApiV1DatasourcesSyncCreateProviderEntityIdErrorComponent
                | ApiV1DatasourcesSyncCreateProviderErrorComponent
                | ApiV1DatasourcesSyncCreateProviderIdErrorComponent
                | ApiV1DatasourcesSyncCreateProviderReferenceErrorComponent
                | ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponent
                | ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponent
                | ApiV1DatasourcesSyncCreateSlaTargetErrorComponent
                | ApiV1DatasourcesSyncCreateSloAvailabilityErrorComponent
                | ApiV1DatasourcesSyncCreateSloTargetErrorComponent
                | ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponent
                | ApiV1DatasourcesSyncCreateTargetAvailabilityErrorComponent
                | ApiV1DatasourcesSyncCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_0 = (
                        ApiV1DatasourcesSyncCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_1 = (
                        ApiV1DatasourcesSyncCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_2 = (
                        ApiV1DatasourcesSyncCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_3 = (
                        ApiV1DatasourcesSyncCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_4 = (
                        ApiV1DatasourcesSyncCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_5 = (
                        ApiV1DatasourcesSyncCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_6 = (
                        ApiV1DatasourcesSyncCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_7 = (
                        ApiV1DatasourcesSyncCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_8 = (
                        ApiV1DatasourcesSyncCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_9 = (
                        ApiV1DatasourcesSyncCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_10 = (
                        ApiV1DatasourcesSyncCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_11 = (
                        ApiV1DatasourcesSyncCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_12 = (
                        ApiV1DatasourcesSyncCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_13 = (
                        ApiV1DatasourcesSyncCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_14 = (
                        ApiV1DatasourcesSyncCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_15 = (
                        ApiV1DatasourcesSyncCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_16 = (
                        ApiV1DatasourcesSyncCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_17 = (
                        ApiV1DatasourcesSyncCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_18 = (
                        ApiV1DatasourcesSyncCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_19 = (
                        ApiV1DatasourcesSyncCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_20 = (
                        ApiV1DatasourcesSyncCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_21 = (
                        ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_22 = (
                        ApiV1DatasourcesSyncCreateDatasourceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_23 = (
                        ApiV1DatasourcesSyncCreateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_24 = (
                        ApiV1DatasourcesSyncCreateSyncIntervalMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_25 = (
                        ApiV1DatasourcesSyncCreateNoteKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_26 = (
                        ApiV1DatasourcesSyncCreateNoteOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_27 = (
                        ApiV1DatasourcesSyncCreateNoteWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_28 = (
                        ApiV1DatasourcesSyncCreateCreateNotesResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_29 = (
                        ApiV1DatasourcesSyncCreateCreateMaintenanceAsDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_30 = (
                        ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_31 = (
                        ApiV1DatasourcesSyncCreateCreateIncidentsWithoutResourcesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_32 = (
                        ApiV1DatasourcesSyncCreateLastSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_sync_create_error_type_33 = (
                        ApiV1DatasourcesSyncCreateLastSyncErrorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_sync_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_datasources_sync_create_error_type_34 = (
                    ApiV1DatasourcesSyncCreateProviderEntityIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_datasources_sync_create_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_datasources_sync_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_datasources_sync_create_validation_error.additional_properties = d
        return api_v1_datasources_sync_create_validation_error

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
