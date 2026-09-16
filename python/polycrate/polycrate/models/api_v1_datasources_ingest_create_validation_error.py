from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_datasources_ingest_create_annotations_error_component import (
        ApiV1DatasourcesIngestCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_archived_at_error_component import (
        ApiV1DatasourcesIngestCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_archived_error_component import (
        ApiV1DatasourcesIngestCreateArchivedErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_archived_reason_error_component import (
        ApiV1DatasourcesIngestCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_create_incidents_error_component import (
        ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_create_incidents_without_resources_error_component import (
        ApiV1DatasourcesIngestCreateCreateIncidentsWithoutResourcesErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_create_maintenance_as_draft_error_component import (
        ApiV1DatasourcesIngestCreateCreateMaintenanceAsDraftErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_create_notes_resolved_error_component import (
        ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_criticality_error_component import (
        ApiV1DatasourcesIngestCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_datasource_url_error_component import (
        ApiV1DatasourcesIngestCreateDatasourceUrlErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_debug_mode_error_component import (
        ApiV1DatasourcesIngestCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_display_name_error_component import (
        ApiV1DatasourcesIngestCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_is_enabled_error_component import (
        ApiV1DatasourcesIngestCreateIsEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_kind_error_component import (
        ApiV1DatasourcesIngestCreateKindErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_labels_error_component import (
        ApiV1DatasourcesIngestCreateLabelsErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_last_sync_error_component import (
        ApiV1DatasourcesIngestCreateLastSyncErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_last_sync_error_error_component import (
        ApiV1DatasourcesIngestCreateLastSyncErrorErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_name_error_component import (
        ApiV1DatasourcesIngestCreateNameErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_non_field_errors_error_component import (
        ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_note_kind_error_component import (
        ApiV1DatasourcesIngestCreateNoteKindErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_note_organization_id_error_component import (
        ApiV1DatasourcesIngestCreateNoteOrganizationIdErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_note_workspace_id_error_component import (
        ApiV1DatasourcesIngestCreateNoteWorkspaceIdErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_platform_service_error_component import (
        ApiV1DatasourcesIngestCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_provider_entity_id_error_component import (
        ApiV1DatasourcesIngestCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_provider_error_component import (
        ApiV1DatasourcesIngestCreateProviderErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_provider_id_error_component import (
        ApiV1DatasourcesIngestCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_provider_reference_error_component import (
        ApiV1DatasourcesIngestCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_reconciliation_enabled_error_component import (
        ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_sla_availability_error_component import (
        ApiV1DatasourcesIngestCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_sla_target_error_component import (
        ApiV1DatasourcesIngestCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_slo_availability_error_component import (
        ApiV1DatasourcesIngestCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_slo_target_error_component import (
        ApiV1DatasourcesIngestCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_sync_interval_minutes_error_component import (
        ApiV1DatasourcesIngestCreateSyncIntervalMinutesErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_target_availability_error_component import (
        ApiV1DatasourcesIngestCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_ingest_create_tolerations_error_component import (
        ApiV1DatasourcesIngestCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DatasourcesIngestCreateValidationError")


@_attrs_define
class ApiV1DatasourcesIngestCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DatasourcesIngestCreateAnnotationsErrorComponent |
            ApiV1DatasourcesIngestCreateArchivedAtErrorComponent | ApiV1DatasourcesIngestCreateArchivedErrorComponent |
            ApiV1DatasourcesIngestCreateArchivedReasonErrorComponent |
            ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponent |
            ApiV1DatasourcesIngestCreateCreateIncidentsWithoutResourcesErrorComponent |
            ApiV1DatasourcesIngestCreateCreateMaintenanceAsDraftErrorComponent |
            ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponent |
            ApiV1DatasourcesIngestCreateCriticalityErrorComponent | ApiV1DatasourcesIngestCreateDatasourceUrlErrorComponent
            | ApiV1DatasourcesIngestCreateDebugModeErrorComponent | ApiV1DatasourcesIngestCreateDisplayNameErrorComponent |
            ApiV1DatasourcesIngestCreateIsEnabledErrorComponent | ApiV1DatasourcesIngestCreateKindErrorComponent |
            ApiV1DatasourcesIngestCreateLabelsErrorComponent | ApiV1DatasourcesIngestCreateLastSyncErrorComponent |
            ApiV1DatasourcesIngestCreateLastSyncErrorErrorComponent | ApiV1DatasourcesIngestCreateNameErrorComponent |
            ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponent | ApiV1DatasourcesIngestCreateNoteKindErrorComponent |
            ApiV1DatasourcesIngestCreateNoteOrganizationIdErrorComponent |
            ApiV1DatasourcesIngestCreateNoteWorkspaceIdErrorComponent |
            ApiV1DatasourcesIngestCreatePlatformServiceErrorComponent |
            ApiV1DatasourcesIngestCreateProviderEntityIdErrorComponent | ApiV1DatasourcesIngestCreateProviderErrorComponent
            | ApiV1DatasourcesIngestCreateProviderIdErrorComponent |
            ApiV1DatasourcesIngestCreateProviderReferenceErrorComponent |
            ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponent |
            ApiV1DatasourcesIngestCreateSlaAvailabilityErrorComponent | ApiV1DatasourcesIngestCreateSlaTargetErrorComponent
            | ApiV1DatasourcesIngestCreateSloAvailabilityErrorComponent |
            ApiV1DatasourcesIngestCreateSloTargetErrorComponent |
            ApiV1DatasourcesIngestCreateSyncIntervalMinutesErrorComponent |
            ApiV1DatasourcesIngestCreateTargetAvailabilityErrorComponent |
            ApiV1DatasourcesIngestCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DatasourcesIngestCreateAnnotationsErrorComponent
        | ApiV1DatasourcesIngestCreateArchivedAtErrorComponent
        | ApiV1DatasourcesIngestCreateArchivedErrorComponent
        | ApiV1DatasourcesIngestCreateArchivedReasonErrorComponent
        | ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponent
        | ApiV1DatasourcesIngestCreateCreateIncidentsWithoutResourcesErrorComponent
        | ApiV1DatasourcesIngestCreateCreateMaintenanceAsDraftErrorComponent
        | ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponent
        | ApiV1DatasourcesIngestCreateCriticalityErrorComponent
        | ApiV1DatasourcesIngestCreateDatasourceUrlErrorComponent
        | ApiV1DatasourcesIngestCreateDebugModeErrorComponent
        | ApiV1DatasourcesIngestCreateDisplayNameErrorComponent
        | ApiV1DatasourcesIngestCreateIsEnabledErrorComponent
        | ApiV1DatasourcesIngestCreateKindErrorComponent
        | ApiV1DatasourcesIngestCreateLabelsErrorComponent
        | ApiV1DatasourcesIngestCreateLastSyncErrorComponent
        | ApiV1DatasourcesIngestCreateLastSyncErrorErrorComponent
        | ApiV1DatasourcesIngestCreateNameErrorComponent
        | ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponent
        | ApiV1DatasourcesIngestCreateNoteKindErrorComponent
        | ApiV1DatasourcesIngestCreateNoteOrganizationIdErrorComponent
        | ApiV1DatasourcesIngestCreateNoteWorkspaceIdErrorComponent
        | ApiV1DatasourcesIngestCreatePlatformServiceErrorComponent
        | ApiV1DatasourcesIngestCreateProviderEntityIdErrorComponent
        | ApiV1DatasourcesIngestCreateProviderErrorComponent
        | ApiV1DatasourcesIngestCreateProviderIdErrorComponent
        | ApiV1DatasourcesIngestCreateProviderReferenceErrorComponent
        | ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponent
        | ApiV1DatasourcesIngestCreateSlaAvailabilityErrorComponent
        | ApiV1DatasourcesIngestCreateSlaTargetErrorComponent
        | ApiV1DatasourcesIngestCreateSloAvailabilityErrorComponent
        | ApiV1DatasourcesIngestCreateSloTargetErrorComponent
        | ApiV1DatasourcesIngestCreateSyncIntervalMinutesErrorComponent
        | ApiV1DatasourcesIngestCreateTargetAvailabilityErrorComponent
        | ApiV1DatasourcesIngestCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_datasources_ingest_create_annotations_error_component import (
            ApiV1DatasourcesIngestCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_archived_at_error_component import (
            ApiV1DatasourcesIngestCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_archived_error_component import (
            ApiV1DatasourcesIngestCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_archived_reason_error_component import (
            ApiV1DatasourcesIngestCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_create_incidents_error_component import (
            ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesIngestCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesIngestCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_criticality_error_component import (
            ApiV1DatasourcesIngestCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_datasource_url_error_component import (
            ApiV1DatasourcesIngestCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_debug_mode_error_component import (
            ApiV1DatasourcesIngestCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_display_name_error_component import (
            ApiV1DatasourcesIngestCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_is_enabled_error_component import (
            ApiV1DatasourcesIngestCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_kind_error_component import (
            ApiV1DatasourcesIngestCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_labels_error_component import (
            ApiV1DatasourcesIngestCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_last_sync_error_component import (
            ApiV1DatasourcesIngestCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_last_sync_error_error_component import (
            ApiV1DatasourcesIngestCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_name_error_component import (
            ApiV1DatasourcesIngestCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_non_field_errors_error_component import (
            ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_note_kind_error_component import (
            ApiV1DatasourcesIngestCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_note_organization_id_error_component import (
            ApiV1DatasourcesIngestCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_note_workspace_id_error_component import (
            ApiV1DatasourcesIngestCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_platform_service_error_component import (
            ApiV1DatasourcesIngestCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_provider_error_component import (
            ApiV1DatasourcesIngestCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_provider_id_error_component import (
            ApiV1DatasourcesIngestCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_provider_reference_error_component import (
            ApiV1DatasourcesIngestCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_sla_availability_error_component import (
            ApiV1DatasourcesIngestCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_sla_target_error_component import (
            ApiV1DatasourcesIngestCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_slo_availability_error_component import (
            ApiV1DatasourcesIngestCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_slo_target_error_component import (
            ApiV1DatasourcesIngestCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesIngestCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_target_availability_error_component import (
            ApiV1DatasourcesIngestCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_tolerations_error_component import (
            ApiV1DatasourcesIngestCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateDatasourceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateSyncIntervalMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateNoteKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateNoteOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateNoteWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateCreateMaintenanceAsDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DatasourcesIngestCreateCreateIncidentsWithoutResourcesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateLastSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesIngestCreateLastSyncErrorErrorComponent):
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
        from ..models.api_v1_datasources_ingest_create_annotations_error_component import (
            ApiV1DatasourcesIngestCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_archived_at_error_component import (
            ApiV1DatasourcesIngestCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_archived_error_component import (
            ApiV1DatasourcesIngestCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_archived_reason_error_component import (
            ApiV1DatasourcesIngestCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_create_incidents_error_component import (
            ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesIngestCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesIngestCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_criticality_error_component import (
            ApiV1DatasourcesIngestCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_datasource_url_error_component import (
            ApiV1DatasourcesIngestCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_debug_mode_error_component import (
            ApiV1DatasourcesIngestCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_display_name_error_component import (
            ApiV1DatasourcesIngestCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_is_enabled_error_component import (
            ApiV1DatasourcesIngestCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_kind_error_component import (
            ApiV1DatasourcesIngestCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_labels_error_component import (
            ApiV1DatasourcesIngestCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_last_sync_error_component import (
            ApiV1DatasourcesIngestCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_last_sync_error_error_component import (
            ApiV1DatasourcesIngestCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_name_error_component import (
            ApiV1DatasourcesIngestCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_non_field_errors_error_component import (
            ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_note_kind_error_component import (
            ApiV1DatasourcesIngestCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_note_organization_id_error_component import (
            ApiV1DatasourcesIngestCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_note_workspace_id_error_component import (
            ApiV1DatasourcesIngestCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_platform_service_error_component import (
            ApiV1DatasourcesIngestCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_provider_entity_id_error_component import (
            ApiV1DatasourcesIngestCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_provider_error_component import (
            ApiV1DatasourcesIngestCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_provider_id_error_component import (
            ApiV1DatasourcesIngestCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_provider_reference_error_component import (
            ApiV1DatasourcesIngestCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_sla_availability_error_component import (
            ApiV1DatasourcesIngestCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_sla_target_error_component import (
            ApiV1DatasourcesIngestCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_slo_availability_error_component import (
            ApiV1DatasourcesIngestCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_slo_target_error_component import (
            ApiV1DatasourcesIngestCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesIngestCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_target_availability_error_component import (
            ApiV1DatasourcesIngestCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_ingest_create_tolerations_error_component import (
            ApiV1DatasourcesIngestCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DatasourcesIngestCreateAnnotationsErrorComponent
                | ApiV1DatasourcesIngestCreateArchivedAtErrorComponent
                | ApiV1DatasourcesIngestCreateArchivedErrorComponent
                | ApiV1DatasourcesIngestCreateArchivedReasonErrorComponent
                | ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponent
                | ApiV1DatasourcesIngestCreateCreateIncidentsWithoutResourcesErrorComponent
                | ApiV1DatasourcesIngestCreateCreateMaintenanceAsDraftErrorComponent
                | ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponent
                | ApiV1DatasourcesIngestCreateCriticalityErrorComponent
                | ApiV1DatasourcesIngestCreateDatasourceUrlErrorComponent
                | ApiV1DatasourcesIngestCreateDebugModeErrorComponent
                | ApiV1DatasourcesIngestCreateDisplayNameErrorComponent
                | ApiV1DatasourcesIngestCreateIsEnabledErrorComponent
                | ApiV1DatasourcesIngestCreateKindErrorComponent
                | ApiV1DatasourcesIngestCreateLabelsErrorComponent
                | ApiV1DatasourcesIngestCreateLastSyncErrorComponent
                | ApiV1DatasourcesIngestCreateLastSyncErrorErrorComponent
                | ApiV1DatasourcesIngestCreateNameErrorComponent
                | ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponent
                | ApiV1DatasourcesIngestCreateNoteKindErrorComponent
                | ApiV1DatasourcesIngestCreateNoteOrganizationIdErrorComponent
                | ApiV1DatasourcesIngestCreateNoteWorkspaceIdErrorComponent
                | ApiV1DatasourcesIngestCreatePlatformServiceErrorComponent
                | ApiV1DatasourcesIngestCreateProviderEntityIdErrorComponent
                | ApiV1DatasourcesIngestCreateProviderErrorComponent
                | ApiV1DatasourcesIngestCreateProviderIdErrorComponent
                | ApiV1DatasourcesIngestCreateProviderReferenceErrorComponent
                | ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponent
                | ApiV1DatasourcesIngestCreateSlaAvailabilityErrorComponent
                | ApiV1DatasourcesIngestCreateSlaTargetErrorComponent
                | ApiV1DatasourcesIngestCreateSloAvailabilityErrorComponent
                | ApiV1DatasourcesIngestCreateSloTargetErrorComponent
                | ApiV1DatasourcesIngestCreateSyncIntervalMinutesErrorComponent
                | ApiV1DatasourcesIngestCreateTargetAvailabilityErrorComponent
                | ApiV1DatasourcesIngestCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_0 = (
                        ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_1 = (
                        ApiV1DatasourcesIngestCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_2 = (
                        ApiV1DatasourcesIngestCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_3 = (
                        ApiV1DatasourcesIngestCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_4 = (
                        ApiV1DatasourcesIngestCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_5 = (
                        ApiV1DatasourcesIngestCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_6 = (
                        ApiV1DatasourcesIngestCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_7 = (
                        ApiV1DatasourcesIngestCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_8 = (
                        ApiV1DatasourcesIngestCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_9 = (
                        ApiV1DatasourcesIngestCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_10 = (
                        ApiV1DatasourcesIngestCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_11 = (
                        ApiV1DatasourcesIngestCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_12 = (
                        ApiV1DatasourcesIngestCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_13 = (
                        ApiV1DatasourcesIngestCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_14 = (
                        ApiV1DatasourcesIngestCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_15 = (
                        ApiV1DatasourcesIngestCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_16 = (
                        ApiV1DatasourcesIngestCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_17 = (
                        ApiV1DatasourcesIngestCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_18 = (
                        ApiV1DatasourcesIngestCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_19 = (
                        ApiV1DatasourcesIngestCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_20 = (
                        ApiV1DatasourcesIngestCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_21 = (
                        ApiV1DatasourcesIngestCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_22 = (
                        ApiV1DatasourcesIngestCreateDatasourceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_23 = (
                        ApiV1DatasourcesIngestCreateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_24 = (
                        ApiV1DatasourcesIngestCreateSyncIntervalMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_25 = (
                        ApiV1DatasourcesIngestCreateNoteKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_26 = (
                        ApiV1DatasourcesIngestCreateNoteOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_27 = (
                        ApiV1DatasourcesIngestCreateNoteWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_28 = (
                        ApiV1DatasourcesIngestCreateCreateNotesResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_29 = (
                        ApiV1DatasourcesIngestCreateCreateMaintenanceAsDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_30 = (
                        ApiV1DatasourcesIngestCreateCreateIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_31 = (
                        ApiV1DatasourcesIngestCreateCreateIncidentsWithoutResourcesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_32 = (
                        ApiV1DatasourcesIngestCreateLastSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_ingest_create_error_type_33 = (
                        ApiV1DatasourcesIngestCreateLastSyncErrorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_ingest_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_datasources_ingest_create_error_type_34 = (
                    ApiV1DatasourcesIngestCreateProviderEntityIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_datasources_ingest_create_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_datasources_ingest_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_datasources_ingest_create_validation_error.additional_properties = d
        return api_v1_datasources_ingest_create_validation_error

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
